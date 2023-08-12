from dataclasses import dataclass

from models.ProductType import ProductType


@dataclass
class CategoryAndScore(object):
    category: ProductType
    score: int | None

    def __lt__(self, other):
        return self.score < other.score


@dataclass
class ProductTypeMetadata:
    from_string: str | None
    categories: [CategoryAndScore]

    def __str__(self):
        return (f"ProductTypeMetadata:\n    category: {self.categories}"
                f"\n    from_string: {self.from_string}")
