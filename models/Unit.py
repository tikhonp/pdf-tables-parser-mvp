from dataclasses import dataclass


@dataclass
class Unit:
    identifier: str
    is_deleted: bool
    code: int
    description: str
    full_name: str
    is_discrete: bool

    def __str__(self):
        return self.full_name
