from pandas import DataFrame


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


def get_product_type(df: DataFrame, column_id: int, row: int) -> str:
    return str(df.iloc[row][column_id])
