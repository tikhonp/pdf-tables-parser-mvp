from dataclasses import dataclass

from models import ProductType, Unit


@dataclass
class FinalRow:
    product_type: ProductType
    unit: Unit
    count: int

    def __str__(self):
        return f"product_type: {self.product_type}, unit: {self.unit}, count: {self.count}"
