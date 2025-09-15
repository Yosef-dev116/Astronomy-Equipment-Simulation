# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025
"""
This class represents a Dobsonian-style mount. It inherits from Mount and
represents a stable, non-computerized base.

"""
from Mount import Mount

class Dobsonian(Mount):
    def __init__(self, motion_type, weight_rating, computerized_goto):
        super().__init__('D', motion_type, 'NA', weight_rating, computerized_goto)
