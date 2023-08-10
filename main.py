import os
import sys
from pathlib import Path

from get_final_rows.get_final_rows import get_final_rows
from get_tables import get_tables
from models.FinalRow import FinalRow
from xml_parser.product_types_parser import product_type_parser
from xml_parser.unit_parser import unit_parser

UNITS_FILE = "/Users/tikhon/Downloads/Справочники1с/ЕдиницыИзмерения1С.xml"
PRODUCT_TYPES_FILE = "/Users/tikhon/Downloads/Справочники1с/Номенклатура1С.xml"


def print_final_rows(rows: [FinalRow]):
    print("\n")
    for row in rows:
        print(*row, sep="\n")
        print("\n")


def parse_input_file() -> Path:
    try:
        return Path(sys.argv[1])
    except IndexError:
        print("Usage: " + os.path.basename(__file__) + " <file path>")
        sys.exit(1)


if __name__ == "__main__":
    print("Parsing input file...")
    file_path = parse_input_file()

    print("Parsing tables...")
    dataframes = get_tables(file_path)
    print("Got dataframes: ", dataframes)

    print("Parsing units...")
    units = unit_parser(Path(UNITS_FILE))

    print("Parsing product types...")
    product_types = product_type_parser(Path(PRODUCT_TYPES_FILE))
    print(len(product_types))

    print("Getting final rows...")
    final_data = [get_final_rows(d, units, product_types) for d in dataframes]

    print_final_rows(final_data)
