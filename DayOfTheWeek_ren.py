import enum
from enum import Enum

"""renpy
init python:
"""


class DayOfTheWeek(Enum):
    """
    An enumeration representing the days of the week.

    Attributes:
        NULL: An undefined value for days that have not been set.
        MONDAY: The first day of the week.
        TUESDAY: The second day of the week.
        WEDNESDAY: The third day of the week.
        THURSDAY: The fourth day of the week.
        FRIDAY: The fifth day of the week.
        SATURDAY: The sixth day of the week.
        SUNDAY: The seventh day of the week.

    Methods:
        _missing_(value: object) -> DayOfTheWeek.NULL:
            A special method called when an undefined value is passed to the enum.
            Returns the NULL value instead of raising a ValueError.
    """

    NULL = enum.auto()
    MONDAY = enum.auto()
    TUESDAY = enum.auto()
    WEDNESDAY = enum.auto()
    THURSDAY = enum.auto()
    FRIDAY = enum.auto()
    SATURDAY = enum.auto()
    SUNDAY = enum.auto()

    @classmethod
    def _missing_(cls, value: object) -> "DayOfTheWeek":
        return cls.NULL
