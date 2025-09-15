# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025

"""
This class defines a Kellner eyepiece. It inherits from the EP base class.

"""

from EP import EP

class Kellner(EP):
    def __init__(self, afov, focal_length):
        super().__init__('K', afov, focal_length)
