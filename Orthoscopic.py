# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025
"""
This class defines an Orthoscopic (Abbe) eyepiece. It inherits from the EP base class.

"""
from EP import EP

class Orthoscopic(EP):
    def __init__(self, afov, focal_length):
        super().__init__('O', afov, focal_length)
