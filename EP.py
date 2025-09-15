# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025
"""
This file defines the abstract base class for Eyepieces. It includes
common properties like apparent field of view (AFOV),focal length, and
eyepiece type. Concrete eyepiece types like Kellner, Nagler, etc. inherit from
this class.
"""


class EP(object):
    def __init__(self, type, afov, focal_length):

        self.__type = type
        self.__afov = afov
        self.__focal_length = focal_length

    def get_type(self):
        return self.__type

    def get_afov(self):
        return self.__afov

    def get_focal_length(self):
        return self.__focal_length

    def __str__(self):
        return (
            "EP\n"
            f"    Type:           {self.get_type()}\n"
            f"    afov:           {self.get_afov()}deg\n"
            f"    Focal Length:   {self.get_focal_length()}mm"
        )
