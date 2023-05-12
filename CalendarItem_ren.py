from __future__ import annotations

from dataclasses import dataclass

from renpy import store

calendar_items: dict[str, CalendarItem]

"""renpy
init python:
"""


@dataclass
class CalendarItem:
    """
    A class representing a to-do item in a calendar.

    Attributes:
        id_ (str): A unique identifier for the to-do item.
        name (str): A display name for the to-do item.
        description (str): A description of the to-do item.
        year (int): The year the to-do item is scheduled for.
        month (int): The month the to-do item is scheduled for.
        day (int): The day the to-do item is scheduled for.
        completed (bool): A flag indicating whether the to-do item has been completed.

    Methods:
        __post_init__() -> None:
            A special method that is called after object initialization.
            Adds the newly created CalendarItem to the calendar_items dictionary in the store.
    """

    id_: str
    name: str
    description: str
    year: int
    month: int
    day: int
    completed: bool = False

    def __post_init__(self) -> None:
        store.calendar_items[self.id_] = self
