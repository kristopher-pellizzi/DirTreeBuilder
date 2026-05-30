from enum import Enum

class TextModifier(Enum):
    NORMAL = "\x1b[0m"
    ITALIC = "\x1b[3m"