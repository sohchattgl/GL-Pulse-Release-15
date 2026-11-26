"""Build the source material for Case study 1, "The Supplier List With a Note Attached".

Release 15, "Every Cell Gets a Receipt". Larkfield Components, its buyers, its notes and
its key are invented. The forty suppliers are real, public component makers and
distributors, named by legal name and public website, because a web-sourced fill needs
public pages. No real person is named anywhere.

Writes into the directory given as the one optional argument, default source_material/
next to this script:

    01_Supplier_List.xlsx   the purchasing export: forty suppliers, headquarters column empty (voice: case)
    02_Supplier_Key.xlsx    the team's key for the two planted suppliers (voice: ours)

Planted rows (the person recording only):

    1. 01_Supplier_List.xlsx, Suppliers tab, row 29, LK-S1066 MISUMI Europa GmbH: a regional
       subsidiary whose parent group, MISUMI Group Inc., has its head office in Tokyo, Japan.
       Our row gives the European company's own website. Headquarters on file: Frankfurt am
       Main, Germany. Serves Part 3.
    2. 01_Supplier_List.xlsx, Suppliers tab, row 37, LK-S1083 Elma Electronic AG: shares its
       trading name with Elma Schmidbauer GmbH, an unrelated maker of ultrasonic cleaners in
       Singen, Germany. Our website column (elma.com) tells them apart. Headquarters on file:
       Wetzikon, Switzerland. Serves Part 3.

Both key entries were checked against the pages named in the key on 26 November 2026.
The person recording re-checks both pages on the day.
"""
import sys
from datetime import datetime
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

HERE = Path(__file__).resolve().parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "source_material"
FIXED = datetime(2026, 11, 26, 9, 0, 0)

KEY_CHECKED = "26 November 2026"
ROWS_FIRST, ROWS_LAST = 3, 42  # data rows on the Suppliers tab

# (account code, legal name, website, entity we buy from, category, buyer, notes)
SUPPLIERS = [
    ("LK-S1004", "Phoenix Contact GmbH & Co. KG", "phoenixcontact.com", "Group", "Terminal blocks, connectors", "D. Whitcombe", "Annual price review in Feb"),
    ("LK-S1007", "TE Connectivity plc", "te.com", "Group", "Connectors", "D. Whitcombe", ""),
    ("LK-S1011", "Molex, LLC", "molex.com", "Group", "Connectors", "S. Nair", "MOQ 500 on most housings"),
    ("LK-S1012", "Amphenol Corporation", "amphenol.com", "Group", "Connectors", "S. Nair", ""),
    ("LK-S1015", "Schneider Electric SE", "se.com", "Group", "Relays, switchgear", "T. Arkwright", "via distributor until 2025, now direct"),
    ("LK-S1018", "Eaton Corporation plc", "eaton.com", "Group", "Circuit protection", "T. Arkwright", ""),
    ("LK-S1020", "Omron Electronics Ltd", "industrial.omron.co.uk", "UK company", "Relays, sensors", "T. Arkwright", "UK sales co invoices us, not the parent"),
    ("LK-S1023", "Murata Manufacturing Co., Ltd.", "murata.com", "Group", "Capacitors", "J. Kowalczyk", ""),
    ("LK-S1024", "TDK Corporation", "tdk.com", "Group", "Inductors, ferrites", "J. Kowalczyk", "lead times 16wks+ !!"),
    ("LK-S1026", "Vishay Intertechnology, Inc.", "vishay.com", "Group", "Resistors, diodes", "J. Kowalczyk", ""),
    ("LK-S1029", "KEMET Electronics Corporation", "kemet.com", "Group", "Capacitors", "J. Kowalczyk", "part of Yageo now, invoices still say KEMET"),
    ("LK-S1031", "Littelfuse, Inc.", "littelfuse.com", "Group", "Fuses", "S. Nair", ""),
    ("LK-S1033", "Bourns, Inc.", "bourns.com", "Group", "Trimmers, circuit protection", "S. Nair", "samples arrive in 2 days usually"),
    ("LK-S1036", "SKF (U.K.) Limited", "skf.com/uk", "UK company", "Bearings", "T. Arkwright", "rebate tier 2 from Q3"),
    ("LK-S1038", "Schaeffler AG", "schaeffler.com", "Group", "Bearings", "T. Arkwright", ""),
    ("LK-S1040", "Bosch Rexroth AG", "boschrexroth.com", "Group", "Linear motion, hydraulics", "T. Arkwright", ""),
    ("LK-S1043", "Festo SE & Co. KG", "festo.com", "Group", "Pneumatics", "D. Whitcombe", ""),
    ("LK-S1045", "SMC Corporation", "smcworld.com", "Group", "Pneumatics", "D. Whitcombe", "check UK stock before ordering"),
    ("LK-S1047", "Parker Hannifin Corporation", "parker.com", "Group", "Fittings, hoses", "D. Whitcombe", ""),
    ("LK-S1050", "WAGO GmbH & Co. KG", "wago.com", "Group", "Terminal blocks", "D. Whitcombe", ""),
    ("LK-S1052", "Weidmüller Interface GmbH & Co. KG", "weidmueller.com", "Group", "Terminal blocks", "D. Whitcombe", "dup of S1009? merged 2023"),
    ("LK-S1055", "HARTING Stiftung & Co. KG", "harting.com", "Group", "Industrial connectors", "S. Nair", "was 'Harting Ltd' in the old system"),
    ("LK-S1057", "Rittal GmbH & Co. KG", "rittal.com", "Group", "Enclosures", "S. Nair", ""),
    ("LK-S1058", "igus GmbH", "igus.eu", "Group", "Cable carriers, plain bearings", "T. Arkwright", ""),
    ("LK-S1061", "U.I. Lapp GmbH", "lapp.com", "Group", "Cable", "S. Nair", "price list due Jan"),
    ("LK-S1063", "Murrelektronik GmbH", "murrelektronik.com", "Group", "Power supplies, IO modules", "S. Nair", ""),
    ("LK-S1066", "MISUMI Europa GmbH", "uk.misumi-ec.com", "EU company", "Shafts, mechanical parts", "T. Arkwright", "orders + invoices from the European company"),
    ("LK-S1068", "Pepperl+Fuchs SE", "pepperl-fuchs.com", "Group", "Sensors", "J. Kowalczyk", ""),
    ("LK-S1070", "ifm electronic gmbh", "ifm.com", "Group", "Sensors", "J. Kowalczyk", ""),
    ("LK-S1072", "Banner Engineering Corp.", "bannerengineering.com", "Group", "Sensors, indicator lights", "J. Kowalczyk", "new 2025"),
    ("LK-S1075", "Sensata Technologies, Inc.", "sensata.com", "Group", "Sensors", "J. Kowalczyk", ""),
    ("LK-S1077", "Belden Inc.", "belden.com", "Group", "Cable, networking", "S. Nair", ""),
    ("LK-S1079", "Panduit Corp.", "panduit.com", "Group", "Cable ties, labels", "S. Nair", ""),
    ("LK-S1081", "Hammond Manufacturing Company Limited", "hammfg.com", "Group", "Enclosures, transformers", "D. Whitcombe", "QUOTES IN CAD"),
    ("LK-S1083", "Elma Electronic AG", "elma.com", "Group", "Subracks, backplanes", "D. Whitcombe", "rack hardware for the defence jobs"),
    ("LK-S1086", "SCHURTER AG", "schurter.com", "Group", "Fuses, power inlets", "S. Nair", ""),
    ("LK-S1088", "Bel Fuse Inc.", "belfuse.com", "Group", "Magnetics, fuses", "S. Nair", ""),
    ("LK-S1090", "MEAN WELL Enterprises Co., Ltd.", "meanwell.com", "Group", "Power supplies", "J. Kowalczyk", "freight terms FOB, ask logistics"),
    ("LK-S1093", "Würth Elektronik eiSos GmbH & Co. KG", "we-online.com", "Group", "Passives, EMC parts", "J. Kowalczyk", ""),
    ("LK-S1095", "RS Components Ltd", "uk.rs-online.com", "UK company", "Catalogue MRO", "T. Arkwright", "card account, top-up orders only"),
]

# The regions tab nobody has maintained since 2024. Inputs only; no headquarters in it.
OLD_REGIONS = [
    ("R1", "UK & Ireland", "GB, IE", "CR-01", "31/03/2025"),
    ("R2", "DACH", "DE, AT, CH", "CR-03", "31/03/2025"),
    ("R3", "Benelux + France", "NL, BE, LU, FR", "CR-03", "31/03/2025"),
    ("R4", "Nordics", "SE, DK, NO, FI", "CR-04", "30/06/2024"),
    ("R5", "Rest of Europe", "", "CR-03", ""),
    ("R6", "North America", "US, CA", "CR-07", "31/12/2024"),
    ("R7", "Asia Pacific", "JP, TW, CN, KR", "CR-07", "31/12/2024"),
]

# The team's key: the two planted suppliers only, as purchasing holds them on file.
KEY = [
    ("LK-S1066", "MISUMI Europa GmbH", "uk.misumi-ec.com", "Frankfurt am Main, Germany",
     "https://uk.misumi-ec.com/en/company/",
     "Regional subsidiary. The parent group, MISUMI Group Inc., has its head office in Tokyo, Japan."),
    ("LK-S1083", "Elma Electronic AG", "elma.com", "Wetzikon, Switzerland",
     "https://www.elma.com/en/who-we-are/company-overview/elma-history",
     "Shared name. Elma Schmidbauer GmbH, an unrelated maker of ultrasonic cleaners, has its head office in Singen, Germany."),
]

HOW_WE_CHECK = [
    "What this key holds: the headquarters our purchasing team keeps on file for two suppliers, and the page that states each one.",
    f"Both pages were read on {KEY_CHECKED}. Whoever records the walkthrough reads both again on the day.",
    "The draw: ten of the forty rows, chosen by a random number that is frozen before the sort.",
    "A row passes when a cited page names the city in the cell as the headquarters and the country matches.",
    "Ten clean rows still allow an error rate of up to about 26% (slide 3.4 of the video).",
    "The note to the logistics lead gives three numbers: rows checked at random, rows matched, and what we did about the rest.",
]

BOLD = Font(bold=True)
HEAD_FILL = PatternFill("solid", fgColor="DDE4EE")


def pin(wb):
    wb.properties.creator = "Larkfield Components"
    wb.properties.lastModifiedBy = "Larkfield Components"
    wb.properties.created = FIXED
    wb.properties.modified = FIXED


def header(ws, row, names, widths):
    for col, (name, width) in enumerate(zip(names, widths), start=1):
        c = ws.cell(row=row, column=col, value=name)
        c.font = BOLD
        c.fill = HEAD_FILL
        ws.column_dimensions[c.column_letter].width = width


def supplier_list(path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Suppliers"
    ws["A1"] = "Larkfield Components | supplier master | purchasing export 24/11/2026 | for Q1 freight review"
    ws["A1"].font = Font(bold=True, size=12)
    header(ws, 2,
           ["Account code", "Legal name", "Website", "Entity we buy from", "Category", "Buyer", "Notes", "HQ city, country"],
           [13, 38, 24, 18, 28, 14, 40, 26])
    for i, rec in enumerate(SUPPLIERS):
        r = ROWS_FIRST + i
        for col, val in enumerate(rec, start=1):
            ws.cell(row=r, column=col, value=val if val != "" else None)
    assert ROWS_FIRST + len(SUPPLIERS) - 1 == ROWS_LAST
    ws.freeze_panes = "A3"

    old = wb.create_sheet("Regions 2024")
    old["A1"] = "freight regions, last updated 03/2024 TA. ask logistics before using!!"
    header(old, 2, ["Region", "Name", "Countries", "Carrier code", "Contract ends"], [8, 20, 22, 13, 14])
    for i, rec in enumerate(OLD_REGIONS):
        for col, val in enumerate(rec, start=1):
            old.cell(row=3 + i, column=col, value=val if val != "" else None)
    old["A11"] = "R8 Middle East? not set up"
    pin(wb)
    wb.save(path)


def supplier_key(path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Key"
    header(ws, 1,
           ["Account code", "Legal name", "Website in our list", "Headquarters on file", "Page that states it", "Why this row is in the key", "Checked"],
           [13, 24, 22, 28, 60, 70, 18])
    for i, rec in enumerate(KEY):
        for col, val in enumerate(rec + (KEY_CHECKED,), start=1):
            c = ws.cell(row=2 + i, column=col, value=val)
            c.alignment = Alignment(wrap_text=True, vertical="top")
    how = wb.create_sheet("How we check")
    how.column_dimensions["A"].width = 110
    for i, line in enumerate(HOW_WE_CHECK, start=1):
        how.cell(row=i, column=1, value=line).alignment = Alignment(wrap_text=True)
    pin(wb)
    wb.save(path)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    built = []
    for name, fn in (("01_Supplier_List.xlsx", supplier_list), ("02_Supplier_Key.xlsx", supplier_key)):
        p = OUT / name
        fn(p)
        print(f"wrote {p}")
        built.append(p)
    print(f"{len(built)} files")


if __name__ == "__main__":
    main()
