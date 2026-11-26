"""
build_materials.py: source material for Case study 2, "A Checking Tab for Every Filled Column".

Halden Outdoor (invented) is an online retailer opening sixty new countries. Its finance analyst
fills currency and standard tax rate for each country with Fill with Gemini, builds a Checking tab
from the finance director's checking policy, samples the currency column, and holds the tax column
against the tax team's rate table.

    python build_materials.py [output folder]      # default: source_material/ beside this script

Files written:
    01_Country_Sheet.xlsx    sixty real countries with region and launch wave; currency and tax rate empty
    02_Tax_Rate_Table.xlsx   the tax team's standard rates, effective 1 November 2026, signed off 3 November 2026
    03_Checking_Policy.docx  the finance director's one-page checking policy, dated 9 November 2026

Where the rates come from. Every standard rate in 02 was checked on 26 November 2026 against
PwC Worldwide Tax Summaries, "Value-added tax (VAT) rates" quick chart
(taxsummaries.pwc.com/quick-charts/value-added-tax-vat-rates), whose rows for these countries were
last reviewed between May and November 2026. Canada, India, Brazil, Malaysia, Ghana, Indonesia,
Vietnam and Thailand were left out because the chart gives a range, a split rate or a temporary
reduction for them. The United States has no national VAT or GST (the chart shows NA). Bulgaria
replaced the lev with the euro on 1 January 2026 (European Commission, Access2Markets notice
"Bulgaria adopts euro as of 1 January 2026"). Recent rate changes noted in 02: Finland 25.5% from
1 September 2024, Slovakia 23% from 1 January 2025, Estonia 24% from 1 July 2025, Romania 21%
from 1 August 2025.

Planted, for the person recording only (matches the case's table):
    1. 02_Tax_Rate_Table.xlsx, Standard rates, United States row: no national rate; the pricing
       model uses 0 and the marketplace partner adds state sales tax at checkout (also in 03).
       Serves Part 4.
    2. 02_Tax_Rate_Table.xlsx, Standard rates, Romania row: 21, changed from 19 on 1 August 2025,
       so older pages still show 19. Serves Part 4.
    3. 02_Tax_Rate_Table.xlsx, Standard rates, Bulgaria row note: prices in EUR since 1 January 2026,
       when the euro replaced the lev, so older pages still show BGN. Serves Part 3 if the draw
       picks Bulgaria, and the Part 4 search.

Deterministic: no random values, no network, fixed document properties.
"""
import sys
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.shared import Pt
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

FIXED = datetime(2026, 11, 16, 9, 0, 0)

# (country, region, launch wave, tax name, standard rate, last change, note)
COUNTRIES = [
    ("United Kingdom", "Europe", "Wave 1", "VAT", 20, "", ""),
    ("Ireland", "Europe", "Wave 1", "VAT", 23, "", ""),
    ("Germany", "Europe", "Wave 1", "VAT", 19, "", ""),
    ("France", "Europe", "Wave 1", "VAT", 20, "", ""),
    ("Netherlands", "Europe", "Wave 1", "VAT", 21, "", ""),
    ("Belgium", "Europe", "Wave 1", "VAT", 21, "", ""),
    ("Austria", "Europe", "Wave 1", "VAT", 20, "", ""),
    ("Switzerland", "Europe", "Wave 1", "VAT", 8.1, "", ""),
    ("Denmark", "Europe", "Wave 1", "VAT", 25, "", ""),
    ("Sweden", "Europe", "Wave 1", "VAT", 25, "", ""),
    ("Norway", "Europe", "Wave 1", "VAT", 25, "", ""),
    ("Finland", "Europe", "Wave 1", "VAT", 25.5, "1 Sep 2024 (was 24)", ""),
    ("United States", "North America", "Wave 1", "None at national level", 0, "",
     "No national VAT or sales tax. Pricing model uses 0; state sales tax is added at checkout "
     "by our marketplace partner. See finance policy of 9 Nov 2026."),
    ("Australia", "Asia Pacific", "Wave 1", "GST", 10, "", ""),
    ("New Zealand", "Asia Pacific", "Wave 1", "GST", 15, "", ""),
    ("Japan", "Asia Pacific", "Wave 1", "Consumption tax", 10, "", ""),
    ("Singapore", "Asia Pacific", "Wave 1", "GST", 9, "", ""),
    ("Italy", "Europe", "Wave 2", "VAT (IVA)", 22, "", ""),
    ("Spain", "Europe", "Wave 2", "VAT (IVA)", 21, "", ""),
    ("Portugal", "Europe", "Wave 2", "VAT (IVA)", 23, "", "Mainland rate. Madeira and Azores lower, not in scope."),
    ("Luxembourg", "Europe", "Wave 2", "VAT", 17, "", ""),
    ("Iceland", "Europe", "Wave 2", "VAT", 24, "", ""),
    ("Poland", "Europe", "Wave 2", "VAT", 23, "", ""),
    ("Czech Republic", "Europe", "Wave 2", "VAT", 21, "", ""),
    ("Slovakia", "Europe", "Wave 2", "VAT", 23, "1 Jan 2025 (was 20)", ""),
    ("Hungary", "Europe", "Wave 2", "VAT", 27, "", ""),
    ("Slovenia", "Europe", "Wave 2", "VAT", 22, "", ""),
    ("Croatia", "Europe", "Wave 2", "VAT", 25, "", "Prices in EUR since 1 Jan 2023."),
    ("Estonia", "Europe", "Wave 2", "VAT", 24, "1 Jul 2025 (was 22)", ""),
    ("Latvia", "Europe", "Wave 2", "VAT", 21, "", ""),
    ("Lithuania", "Europe", "Wave 2", "VAT", 21, "", ""),
    ("South Korea", "Asia Pacific", "Wave 2", "VAT", 10, "", ""),
    ("United Arab Emirates", "Middle East and Africa", "Wave 2", "VAT", 5, "", ""),
    ("Israel", "Middle East and Africa", "Wave 2", "VAT", 18, "", ""),
    ("Mexico", "Latin America", "Wave 2", "VAT (IVA)", 16, "", "General rate. Border region rate not used."),
    ("Chile", "Latin America", "Wave 2", "VAT (IVA)", 19, "", ""),
    ("Romania", "Europe", "Wave 3", "VAT", 21, "1 Aug 2025 (was 19)", ""),
    ("Bulgaria", "Europe", "Wave 3", "VAT", 20, "",
     "Prices in EUR since 1 Jan 2026, when the euro replaced the lev."),
    ("Greece", "Europe", "Wave 3", "VAT", 24, "", ""),
    ("Cyprus", "Europe", "Wave 3", "VAT", 19, "", ""),
    ("Malta", "Europe", "Wave 3", "VAT", 18, "", ""),
    ("Albania", "Europe", "Wave 3", "VAT", 20, "", ""),
    ("Serbia", "Europe", "Wave 3", "VAT", 20, "", ""),
    ("Turkey", "Europe", "Wave 3", "VAT (KDV)", 20, "", ""),
    ("Colombia", "Latin America", "Wave 3", "VAT (IVA)", 19, "", ""),
    ("Peru", "Latin America", "Wave 3", "IGV", 18, "", "16 IGV plus 2 municipal promotion tax, charged together."),
    ("Argentina", "Latin America", "Wave 3", "VAT (IVA)", 21, "", ""),
    ("Uruguay", "Latin America", "Wave 3", "VAT (IVA)", 22, "", ""),
    ("Costa Rica", "Latin America", "Wave 3", "VAT (IVA)", 13, "", ""),
    ("Dominican Republic", "Latin America", "Wave 3", "ITBIS", 18, "", ""),
    ("Philippines", "Asia Pacific", "Wave 3", "VAT", 12, "", ""),
    ("Saudi Arabia", "Middle East and Africa", "Wave 3", "VAT", 15, "", ""),
    ("Bahrain", "Middle East and Africa", "Wave 3", "VAT", 10, "", ""),
    ("Oman", "Middle East and Africa", "Wave 3", "VAT", 5, "", ""),
    ("South Africa", "Middle East and Africa", "Wave 3", "VAT", 15, "", ""),
    ("Kenya", "Middle East and Africa", "Wave 3", "VAT", 16, "", ""),
    ("Morocco", "Middle East and Africa", "Wave 3", "VAT", 20, "", ""),
    ("Egypt", "Middle East and Africa", "Wave 3", "VAT", 14, "", ""),
    ("Nigeria", "Middle East and Africa", "Wave 3", "VAT", 7.5, "", ""),
    ("Tunisia", "Middle East and Africa", "Wave 3", "VAT", 19, "", ""),
]

EFFECTIVE = "1 November 2026"
SIGNED_OFF = "3 November 2026"
MEMO_DATE = "9 November 2026"
SHEET_DATE = "16 November 2026"

BOLD = Font(bold=True)
HEAD_FILL = PatternFill("solid", fgColor="DDE6EE")


def header(ws, cells, widths):
    ws.append(cells)
    for i, w in enumerate(widths, start=1):
        c = ws.cell(row=1, column=i)
        c.font = BOLD
        c.fill = HEAD_FILL
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.column_dimensions[c.column_letter].width = w
    ws.freeze_panes = "A2"


def pin(wb):
    wb.properties.creator = "Halden Outdoor Finance"
    wb.properties.lastModifiedBy = "Halden Outdoor Finance"
    wb.properties.created = FIXED
    wb.properties.modified = FIXED


def country_sheet(path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Countries"
    header(ws, ["Country", "Region", "Launch wave", "Currency", "Standard tax rate (%)"], [24, 24, 13, 12, 20])
    for c in COUNTRIES:
        ws.append([c[0], c[1], c[2], None, None])
    notes = wb.create_sheet("Notes")
    notes.column_dimensions["A"].width = 100
    for line in [
        "Country sheet, new markets 2027-28",
        f"Started {SHEET_DATE} by finance (analyst). Regions and waves from the Ops launch plan v3.",
        "Currency + Standard tax rate (%) still to fill. Controller wants it by Friday for local list prices.",
        "Wave 1 = first half 2027, Wave 2 = second half 2027, Wave 3 = 2028 (dates TBC by Ops, don't quote them).",
        "Canada, India, Brazil etc parked for now, tax is too messy for a single rate. Ask tax team before adding.",
        "Please don't re-sort the Countries tab, Ops reads it in wave order.",
    ]:
        notes.append([line])
    pin(wb)
    wb.save(path)


def tax_table(path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Standard rates"
    header(ws, ["Country", "Tax", "Standard rate (%)", "Last change", "Note"], [24, 24, 18, 22, 70])
    for c in sorted(COUNTRIES, key=lambda r: r[0]):
        ws.append([c[0], c[3], c[4], c[5] or None, c[6] or None])
    for row in ws.iter_rows(min_row=2, min_col=5, max_col=5):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    so = wb.create_sheet("Sign-off")
    so.column_dimensions["A"].width = 28
    so.column_dimensions["B"].width = 80
    for k, v in [
        ("Table", "Standard VAT / GST rates for new-market pricing"),
        ("Rates in force on", EFFECTIVE),
        ("Signed off by", "Halden tax team"),
        ("Signed off on", SIGNED_OFF),
        ("Countries", len(COUNTRIES)),
        ("Use", "This table is the only approved source for tax rates in the pricing model. "
                "Standard rate only; reduced rates are handled per product line."),
        ("Next review", "1 February 2027, or sooner if a rate changes"),
        ("Questions", "Tax team, Halden Outdoor (internal)"),
    ]:
        so.append([k, v])
        so.cell(row=so.max_row, column=1).font = BOLD
    pin(wb)
    wb.save(path)


def policy(path):
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    doc.add_heading("Memo: checking anything Gemini fills", level=1)
    for k, v in [
        ("To", "Finance team"),
        ("Cc", "Finance controller"),
        ("From", "Ilse Marchetti, Finance Director"),
        ("Date", MEMO_DATE),
        ("Subject", "How much we check, by what the column is for"),
    ]:
        p = doc.add_paragraph()
        p.add_run(f"{k}: ").bold = True
        p.add_run(v)
    doc.add_paragraph(
        "We are now using Fill with Gemini in Sheets for the new-markets work, and it is quick. "
        "That is the problem as much as the point. A sheet that fills itself in a minute looks finished, "
        "and nobody is going to open every source on 60 or 600 rows. So from today, every filled column "
        "gets a tier before anyone checks it, and the tier says how much checking it gets."
    )
    doc.add_heading("The four tiers", level=2)
    t = doc.add_table(rows=1, cols=4)
    t.style = "Table Grid"
    for i, h in enumerate(["How the column is used", "What we check", "What a clean result tells us", "Does Gemini fill it?"]):
        t.rows[0].cells[i].text = h
        t.rows[0].cells[i].paragraphs[0].runs[0].bold = True
    for row in [
        ("First look (is the prompt working?)", "5 random cells",
         "Only that the prompt and format work. Five clean cells still allow up to 45% wrong.", "Yes"),
        ("A list the team works from", "30 random cells",
         "Fewer than 1 in 10 wrong. About half an hour at under a minute a cell.", "Yes"),
        ("A figure that changes a decision", "Every cell's source",
         "Each value was found on its page. If that is too many cells, the sheet is too big for that use.",
         "Yes, if we open every source"),
        ("A figure we must defend (prices, tax rates, anything in the pricing model)",
         "A formula from an approved table", "Each number has a formula trail back to the table.",
         "No. Gemini may label around it, never fill it."),
    ]:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = v
    doc.add_paragraph()
    doc.add_paragraph(
        "For reference, what a clean random sample still allows: 5 clean cells, up to 45% wrong; "
        "10 clean, about 26%; 20 clean, about 14%; 30 clean, under 10%. Random means random: give every "
        "row a random number, freeze it, sort by it and check from the top. Not the first rows of the list."
    )
    doc.add_paragraph(
        "If any sampled cell fails, the whole column is checked cell by cell before it leaves finance."
    )
    doc.add_heading("How this applies to the new-markets country sheet", level=2)
    doc.add_paragraph(
        "Currency is a list the team works from: 30 random cells, pass or fail against the cited page."
    )
    doc.add_paragraph(
        "The standard tax rate goes straight into local list prices, so it is a figure we must defend. "
        "It comes from the tax team's rate table (effective 1 November 2026) by lookup, full stop. "
        "Where a country has no national rate (the United States), the pricing model uses 0 and our "
        "marketplace partner adds state sales tax at checkout."
    )
    doc.add_heading("Recommendation", level=2)
    doc.add_paragraph(
        "Put a Checking tab in every sheet Gemini fills, with these tiers in it, so the answer to "
        "'how much did you check?' is on the sheet and not in someone's head. Controller signs off "
        "nothing that reaches pricing without it."
    )
    doc.add_paragraph("Ilse")
    cp = doc.core_properties
    cp.author = "Ilse Marchetti"
    cp.last_modified_by = "Ilse Marchetti"
    cp.created = FIXED
    cp.modified = FIXED
    cp.revision = 1
    doc.save(path)


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "source_material"
    out.mkdir(parents=True, exist_ok=True)
    assert len(COUNTRIES) == 60, len(COUNTRIES)
    assert len({c[0] for c in COUNTRIES}) == 60
    written = []
    for name, fn in [
        ("01_Country_Sheet.xlsx", country_sheet),
        ("02_Tax_Rate_Table.xlsx", tax_table),
        ("03_Checking_Policy.docx", policy),
    ]:
        p = out / name
        fn(p)
        written.append(p)
        print(f"wrote {p}")
    print(f"{len(written)} files")


if __name__ == "__main__":
    main()
