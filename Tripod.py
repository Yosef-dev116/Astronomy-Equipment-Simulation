# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025
"""
This class defines a standard Tripod mount. It supports motion types and
Go-To functionality.It inherits from the Mount abstract base class.

"""

from Mount import Mount

class Tripod(Mount):
    def __init__(self, physical_type, motion_type, mount_plate_type, weight_rating, computerized_goto):
        super().__init__(physical_type, motion_type, mount_plate_type, weight_rating, computerized_goto)
