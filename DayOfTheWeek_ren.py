"""renpy
init python:
"""

import enum
from enum import Enum


class DayOfTheWeek(Enum):
    NULL = enum.auto()
    MONDAY = enum.auto()
    TUESDAY = enum.auto()
    WEDNESDAY = enum.auto()
    THURSDAY = enum.auto()
    FRIDAY = enum.auto()
    SATURDAY = enum.auto()
    SUNDAY = enum.auto()
