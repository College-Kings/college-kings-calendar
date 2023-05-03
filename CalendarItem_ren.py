from dataclasses import dataclass

from renpy import store

"""renpy
init python:
"""


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
