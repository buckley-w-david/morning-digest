import enum

from .base_source import Source, SourceContent
from .monkeyuser import MonkeyUser
from .xkcd import XKCD


class SourceType(enum.Enum):
    MONKEYUSER = enum.auto()
    XKCD = enum.auto()

    @staticmethod
    def from_name(name: str) -> "SourceType":
        return getattr(SourceType, name.upper().strip())

ALL_SOURCES = [t.name for t in SourceType]
TYPE_MAP = {
    SourceType.MONKEYUSER: MonkeyUser,
    SourceType.XKCD: XKCD,
}
