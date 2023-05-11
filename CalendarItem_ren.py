from __future__ import annotations

from dataclasses import dataclass

from renpy import store

calendar_items: dict[str, CalendarItem]

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

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, CalendarItem):
            return NotImplemented

        return self.id_ == __value.id_
