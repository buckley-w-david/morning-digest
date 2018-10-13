import enum

from .base_component import Component, ComponentContent
from .monkeyuser import MonkeyUserComponent
from .xkcd import XKCDComponent


class ComponentType(enum.Enum):
    MONKEYUSER = enum.auto()
    XKCD = enum.auto()

    @staticmethod
    def from_name(name: str) -> "ComponentType":
        return getattr(ComponentType, name.upper().strip())


ALL_COMPONENTS = [t.name for t in ComponentType]
