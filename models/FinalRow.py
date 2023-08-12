from dataclasses import dataclass

from models import ProductType, Unit
from models.ProductTypeMetadata import ProductTypeMetadata


@dataclass
class FinalRow:
    product_type: ProductTypeMetadata
    unit: Unit
    count: int

    def __str__(self):
        return f"{self.product_type}\nUnit: {self.unit}, Count: {self.count}"
