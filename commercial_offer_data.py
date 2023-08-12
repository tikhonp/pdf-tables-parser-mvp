from fuzzywuzzy import fuzz
from pandas import DataFrame
from tqdm import tqdm

from models.FinalRow import FinalRow
from models.ProductType import ProductType
from models.ProductTypeMetadata import ProductTypeMetadata, CategoryAndScore
from models.Unit import Unit


class CommercialOfferData:
    df: DataFrame
    units: [Unit]
    product_types: [ProductType]
    first_data_row_id: int

    def __init__(self, df: DataFrame, units: [Unit], product_types: [ProductType]):
        self.df = df
        self.units = units
        self.product_types = product_types
        self.first_data_row_id = len(df)

    def find_column(self, *tags: [str]) -> int | None:
        """Returns column index and stores first data row id"""

        column_id = None
        from_row_id = self.first_data_row_id
        for i in range(0, len(self.df)):
            if column_id is None:
                for index, element in enumerate(self.df.iloc[i]):
                    if element is not None and any(map(lambda x: x in element.lower(), tags)):
                        column_id = index
                        from_row_id = i + 1
                        break
            else:
                if self.df.iloc[i][column_id] is not None and not any(
                        map(lambda x: x in self.df.iloc[i][column_id].lower(), tags)):
                    from_row_id = i

                    self.first_data_row_id = min(self.first_data_row_id, from_row_id)
                    return column_id

        self.first_data_row_id = min(self.first_data_row_id, from_row_id)
        return column_id

    def find_product_type(self, tag: str) -> ProductTypeMetadata | None:
        calculated_scores = [
            CategoryAndScore(
                category=c,
                score=fuzz.WRatio(tag.lower(), c.full_name.lower()) + fuzz.WRatio(
                    tag.lower(), c.wrapped_description.lower())
            ) for c in tqdm(self.product_types)
        ]
        return ProductTypeMetadata(
            from_string=tag,
            categories=sorted(calculated_scores, reverse=True)[:5],
        )

    def get_product_type(self, column_id: int | None, row: int) -> ProductTypeMetadata | None:
        tag = self.df.iloc[row][column_id] if isinstance(column_id, int) else None
        if isinstance(tag, str):
            return self.find_product_type(tag)
        else:
            return None

    def find_unit(self, tag: str) -> Unit | None:
        current_max_rate_unit = None
        current_rate = 0

        for u in self.units:
            unit_tag = ""
            if isinstance(u.full_name, str):
                unit_tag = u.full_name
            elif isinstance(u.description, str):
                unit_tag = u.description

            ratio = fuzz.WRatio(tag.lower(), unit_tag.lower())
            if ratio > current_rate:
                current_max_rate_unit = u
                current_rate = ratio

        return current_max_rate_unit

    def get_unit(self, column_id: int | None, row: int) -> Unit | None:
        tag = self.df.iloc[row][column_id] if isinstance(column_id, int) else None
        if isinstance(tag, str):
            return self.find_unit(tag)
        else:
            return None

    def get_count(self, column_id: int, row: int) -> int | None:
        element = self.df.iloc[row][column_id] if isinstance(column_id, int) else None
        if isinstance(element, str) and element.isdigit():
            return int(element)
        else:
            return None

    def get_final_rows(self) -> [FinalRow]:
        if self.first_data_row_id == len(self.df):
            self.first_data_row_id = 0

        unit_column_id = self.find_column("изм")
        product_type_column_id = self.find_column("наименование", "продукт", "товар")
        count_column_id = self.find_column("кол-во", "кол")

        return [FinalRow(product_type=self.get_product_type(product_type_column_id, i),
                         unit=self.get_unit(unit_column_id, i), count=self.get_count(count_column_id, i)) for i in
                range(self.first_data_row_id, len(self.df))]
