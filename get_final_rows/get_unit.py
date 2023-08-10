from pandas import DataFrame

from models.Unit import Unit

from fuzzywuzzy import fuzz


def find_unit_column(df: DataFrame) -> (int, int):
    """returns: (column id, from row id)"""

    tags = ("изм")
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


def find_unit(tag: str, units: [Unit]) -> Unit | None:
    current_max_rate_unit = None
    current_rate = 0

    for u in units:
        ratio = fuzz.WRatio(tag.lower(), u.full_name.lower())
        if ratio > current_rate:
            current_max_rate_unit = u
            current_rate = ratio

    return current_max_rate_unit


def get_unit(df: DataFrame, column_id: int, row: int, units: [Unit]) -> Unit:
    return find_unit(df.iloc[row][column_id], units)
