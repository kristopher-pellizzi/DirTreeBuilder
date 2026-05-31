import logging

from math import floor
from enum import Enum

_logger = logging.getLogger(__name__)

class SizeUnit(Enum):
    BYTES = "B"
    KILOBYTES = "KB"
    MEGABYTES = "MB"
    GIGABYTES = "GB"
    TERABYTES = "TB"

    @classmethod
    def compute_unit(cls, size):
        _logger.debug(f"Start computing unit for size {size}")
        current = int(size)
        current_rem = 0

        for unit in cls:
            _logger.debug(f"Considered unit is {unit}")
            # reminder represents the number of current unit not forming a whole bigger unit (e.g. number of remined bytes after forming N KB => Divide by 1024 to find the correct decimal value)
            remainder = current & 1023
            int_part = current >> 10
            _logger.debug(f"Shifted current evaluates to {int_part}")
            if int_part < 1 or unit == cls.TERABYTES:
                _logger.debug(f"Returning unit {unit}")
                float_size = current + (current_rem / 1024)
                ret_size = round(float_size, 2)
                if floor(float_size) == ret_size:
                    ret_size = floor(ret_size)

                return ret_size, unit

            current = int_part
            current_rem = remainder