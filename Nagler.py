# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025

"""
This class defines a Nagler eyepiece. Known for wide field of view, it inherits from EP.

"""
from EP import EP

class Nagler(EP):
    def __init__(self, afov, focal_length):
        super().__init__('N', afov, focal_length)
