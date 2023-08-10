from pandas import DataFrame

from get_final_rows.get_count import find_count_column, get_count
from get_final_rows.get_product_type import find_product_type_column, get_product_type
from get_final_rows.get_unit import find_unit_column, get_unit
from models import FinalRow, Unit, ProductType


def get_final_rows(df: DataFrame, units: [Unit], product_types: [ProductType]) -> [FinalRow]:
    unit_column_id, unit_first_row_id = find_unit_column(df)
    product_type_column_id, product_type_row_id = find_product_type_column(df)
    count_column_id, count_row_id = find_count_column(df)

    return [
        FinalRow(
            product_type=get_product_type(df, product_type_column_id, i),
            unit=get_unit(df, unit_column_id, i, units),
            count=get_count(df, count_column_id, i),
        ) for i in range(min(unit_first_row_id, product_type_row_id, count_row_id), len(df))
    ]
