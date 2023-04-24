import enum
from enum import Enum

"""renpy
init python:
"""


class DayOfTheWeek(Enum):
    NULL = enum.auto()
    MONDAY = enum.auto()
    TUESDAY = enum.auto()
    WEDNESDAY = enum.auto()
    THURSDAY = enum.auto()
    FRIDAY = enum.auto()
    SATURDAY = enum.auto()
    SUNDAY = enum.auto()

    @classmethod
    def _missing_(cls, value):
        return cls.NULL
