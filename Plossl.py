# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025

"""
This class defines a Plössl eyepiece. It inherits from the EP base class.

"""

from EP import EP

class Plossl(EP):
    def __init__(self, afov, focal_length):
        super().__init__('P', afov, focal_length)
