import enum
from enum import Enum


@enum.unique
class PageLanguage(str, Enum):
    CZ = "cs"
    EN = "en"
