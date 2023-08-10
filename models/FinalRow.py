from dataclasses import dataclass

from models import ProductType, Unit


@dataclass
class FinalRow:
    product_type: ProductType
    unit: Unit
    count: int
