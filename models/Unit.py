from dataclasses import dataclass


@dataclass
class Unit:
    identifier: str
    is_deleted: bool
    code: int
    description: str
    full_name: str
    is_discrete: bool
