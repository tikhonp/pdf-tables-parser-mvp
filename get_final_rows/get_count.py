from pandas import DataFrame


def find_count_column(df: DataFrame) -> (int, int):
    """returns: (column id, from row id)"""

    tags = ("кол-во", "кол")
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


def get_count(df: DataFrame, column_id: int, row: int) -> int | None:
    element = df.iloc[row][column_id]
    if element.isDisgit():
        return int(element)
    else:
        return None
