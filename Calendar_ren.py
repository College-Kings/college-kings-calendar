import datetime
from typing import Optional

from renpy import store

from game.calendar.CalendarItem_ren import CalendarItem

calendar_now: datetime.datetime
calendar_checklist: dict[tuple[int, int, int], list[CalendarItem]]
calendar_items: dict[str, CalendarItem]

"""renpy
init python:
"""


class Calendar:
    """
    A class for managing a calendar and its associated to-do items.

    Attributes:
        MONTH_DAYS (list[int]): A list of the number of days in each month, where the first element is 0.

    Methods:
        is_leap_year(year: int) -> bool:
            Determines if a given year is a leap year or not.
            Returns True if it is a leap year, False otherwise.

        month_range(year: int, month: int) -> tuple[int, int]:
            Calculates the weekday (0-6 ~ Mon-Sun) and number of days (28-31) for a given year and month.
            Raises an Exception if month is not between 1-12.
            Returns a tuple containing the weekday and number of days.

        add_todo(year: int, month: int, day: int, id_: str, display_name: str, description: str = "") -> CalendarItem:
            Adds a to-do item to the calendar for the given year, month, and day.
            Returns the newly created CalendarItem.

        complete_todo(id_: str) -> CalendarItem:
            Marks the specified to-do item as completed.
            Returns the updated CalendarItem.

        remove_todo(id_: str) -> None:
            Removes the specified to-do item from the calendar.

        add_days(number_of_days: int = 1) -> None:
            Advances the calendar by the specified number of days.

        set_date(year: int, month: int, day: int) -> None:
            Sets the current date of the calendar to the specified date.
            Equivalent to set_time().
            Deprecated in favor of add_days().

        contains(id_: str) -> bool:
            Determines if the specified to-do item is present in the calendar.
            Returns True if it is present, False otherwise.

        find(id_: str) -> Optional[CalendarItem]:
            Returns the CalendarItem corresponding to the specified ID, if present in the calendar.
            Returns None otherwise.
    """

    MONTH_DAYS: list[int] = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Return True for leap years, False for non-leap years."""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def month_range(year: int, month: int) -> tuple[int, int]:
        """Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for
        year, month."""

        if not 1 <= month <= 12:
            raise Exception(f"bad month number {month}; must be 1-12")

        day1: int = datetime.date(year, month, 1).weekday()
        number_of_days: int = Calendar.MONTH_DAYS[month] + (
            month == 2 and Calendar.is_leap_year(year)
        )
        return day1, number_of_days

    @staticmethod
    def add_todo(
        year: int,
        month: int,
        day: int,
        id_: str,
        display_name: str,
        description: str = "",
    ) -> CalendarItem:
        calendar_item = CalendarItem(id_, display_name, description, year, month, day)
        calendar_checklist.setdefault((year, month, day), []).append(calendar_item)
        return calendar_item

    @staticmethod
    def complete_todo(id_: str) -> CalendarItem:
        calendar_item: CalendarItem = calendar_items[id_]
        calendar_item.completed = True
        return calendar_item

    @staticmethod
    def remove_todo(id_: str) -> None:
        item: CalendarItem = calendar_items[id_]
        calendar_checklist[item.day, item.month, item.year].remove(item)
        del calendar_items[id_]

    @staticmethod
    def add_days(number_of_days: int = 1) -> None:
        store.calendar_now += datetime.timedelta(days=number_of_days)

    # DEPRICATED
    @staticmethod
    def set_time(year: int, month: int, day: int) -> None:
        store.calendar_now = datetime.datetime(year, month, day)

    @staticmethod
    def set_date(year: int, month: int, day: int) -> None:
        store.calendar_now = datetime.datetime(year, month, day)

    @staticmethod
    def contains(id_: str) -> bool:
        return id_ in calendar_items

    @staticmethod
    def find(id_: str) -> Optional[CalendarItem]:
        return calendar_items.get(id_, None)
