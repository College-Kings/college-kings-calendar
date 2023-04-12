"""renpy
init python:
"""

from __future__ import annotations
import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.calendar.CalendarItem_ren import CalendarItem
    from renpy import store


class Calendar:
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
        store.calendar_checklist.setdefault((year, month, day), []).append(
            calendar_item
        )
        return calendar_item

    @staticmethod
    def complete_todo(id_: str) -> CalendarItem:
        calendar_item: CalendarItem = store.calendar_items[id_]
        calendar_item.completed = True
        return calendar_item

    @staticmethod
    def remove_todo(id_: str) -> None:
        item: CalendarItem = store.calendar_items[id_]
        store.calendar_checklist[item.day, item.month, item.year].remove(item)
        del store.calendar_items[id_]

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
        return id_ in store.calendar_items

    @staticmethod
    def find(id_: str) -> CalendarItem:
        return store.calendar_items.get(id_, None)
