from fuzzywuzzy import fuzz
from pandas import DataFrame
from tqdm import tqdm

from models.ProductType import ProductType


def find_product_type_column(df: DataFrame) -> (int, int):
    """Returns column index and first data row index"""

    tags = ("наименование", "продукт")

    column_id = None
    from_row_id = None
    for i in range(0, len(df)):
        if column_id is None:
            for index, element in enumerate(df.iloc[i]):
                if element is not None and any(map(lambda x: x in element.lower(), tags)):
                    column_id = index
                    from_row_id = i + 1
                    break
        else:
            if df.iloc[i][column_id] is not None and not any(map(lambda x: x in df.iloc[i][column_id].lower(), tags)):
                from_row_id = i
                return column_id, from_row_id

    return column_id, from_row_id


def find_product_type(tag: str, product_types: [ProductType]) -> ProductType | None:
    current_max_rate_product_type = None
    current_rate = 0

    for n in tqdm(product_types):
        ratio = fuzz.WRatio(tag.lower(), n.full_name.lower())
        if ratio > current_rate:
            current_max_rate_product_type = n
            current_rate = ratio

    return current_max_rate_product_type


def get_product_type(df: DataFrame, column_id: int, row: int, product_types: [ProductType]) -> ProductType | None:
    return find_product_type(str(df.iloc[row][column_id]), product_types)
