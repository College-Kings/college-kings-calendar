"""renpy
init python:
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from renpy import store


@dataclass
class CalendarItem:
    id_: str
    name: str
    description: str
    year: int
    month: int
    day: int
    completed: bool = False

    def __post_init__(self) -> None:
        store.calendar_items[self.id_] = self
