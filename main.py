import os
import sys
from pathlib import Path

from pandas import DataFrame

from commercial_offer_data import CommercialOfferData
from get_tables import get_tables
from models.FinalRow import FinalRow
from xml_parser.product_types_parser import product_type_parser
from xml_parser.unit_parser import unit_parser

UNITS_FILE = "/Users/tikhon/Downloads/Справочники1с/ЕдиницыИзмерения1С.xml"
PRODUCT_TYPES_FILE = "/Users/tikhon/Downloads/Справочники1с/Номенклатура1С.xml"


def print_final_rows_to_file(file_path: Path, rows: [FinalRow]):
    with open(file_path, 'w') as f:
        for row in rows:
            print(*row, sep="\n", file=f)
            print("\n", file=f)


def print_final_rows(rows: [FinalRow]):
    print("\n")
    for row in rows:
        print(*row, sep="\n")
        print("\n")
    print("\n\n")


def parse_input_file() -> Path:
    try:
        return Path(sys.argv[1])
    except IndexError:
        print("Usage: " + os.path.basename(__file__) + " <file path>")
        sys.exit(1)


def generate_data_for_df(rows: [FinalRow]) -> list:
    return [
        [
            getattr(r.product_type, 'from_string', None),
            str(r.product_type.categories[0].category) if r.product_type is not None else None,
            str(r.product_type.categories[1].category) if r.product_type is not None else None,
            str(r.product_type.categories[2].category) if r.product_type is not None else None,
            str(r.product_type.categories[3].category) if r.product_type is not None else None,
            str(r.product_type.categories[4].category) if r.product_type is not None else None,
            r.product_type.categories[0].score if r.product_type is not None else None,
            r.product_type.categories[1].score if r.product_type is not None else None,
            r.product_type.categories[2].score if r.product_type is not None else None,
            r.product_type.categories[3].score if r.product_type is not None else None,
            r.product_type.categories[4].score if r.product_type is not None else None,
            str(r.unit),
            r.count,
        ] for r in rows
    ]


def main_save_to_csv():
    print("Parsing units...")
    units = unit_parser(Path(UNITS_FILE))

    print("Parsing product types...")
    product_types = product_type_parser(Path(PRODUCT_TYPES_FILE))

    output_data = []

    for i in range(1, 52):
        file_path = f"/Users/tikhon/Downloads/КП/{i}.pdf"

        print("PARSING ", file_path)

        print("Parsing tables...")
        dataframes = get_tables(Path(file_path))
        print("Got dataframes: ", dataframes)

        print("Getting final rows...")
        for d in dataframes:
            output_data += generate_data_for_df(
                CommercialOfferData(d, units, product_types).get_final_rows()
            )
    df = DataFrame(output_data,
                   columns=["from_string", "category_1", "category_2", "category_3", "category_4", "category_5",
                            "score_1", "score_2", "score_3", "score_4", "score_5", "unit", "count"])
    df.to_csv("~/Desktop/out.csv")


def main():
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
    final_data = [CommercialOfferData(d, units, product_types).get_final_rows() for d in dataframes]

    print_final_rows(final_data)


def main_parse_all_files():
    print("Parsing units...")
    units = unit_parser(Path(UNITS_FILE))

    print("Parsing product types...")
    product_types = product_type_parser(Path(PRODUCT_TYPES_FILE))

    for i in range(1, 52):
        file_path = f"/Users/tikhon/Downloads/КП/{i}.pdf"
        output_file_path = f"/Users/tikhon/Downloads/КП/{i}.txt"

        print("PARSING ", file_path)

        print("Parsing tables...")
        dataframes = get_tables(Path(file_path))
        print("Got dataframes: ", dataframes)

        print("Getting final rows...")
        final_data = [CommercialOfferData(d, units, product_types).get_final_rows() for d in dataframes]

        print_final_rows(final_data)

        print_final_rows_to_file(Path(output_file_path), final_data)


if __name__ == "__main__":
    main_save_to_csv()
