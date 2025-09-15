# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025

"""
This is the abstract base class for telescope mounts. It stores shared mount
properties such as motion type, weight rating, computerized tracking (Go-To),
and mount plate type. Specific mount types like Tripod and Dobsonian inherit from this.
"""

from OpticalToolbox import OpticalToolbox
class Mount(OpticalToolbox):
    def __init__(self, physical_type, motion_type, mount_plate_type, weight_rating, computerized_goto):
        self.__physical_type = physical_type
        self.__motion_type = motion_type
        self.__mount_plate_type = mount_plate_type
        self.__weight_rating = weight_rating
        self.__computerized_goto = computerized_goto  # should be True/False

    def get_physical_type(self):
        return self.__physical_type

    def get_motion_type(self):
        return self.__motion_type

    def get_mount_plate_type(self):
        return self.__mount_plate_type

    def get_weight_rating(self):
        return self.__weight_rating

    def has_computerized_goto(self):
        return self.__computerized_goto

    def __str__(self):
        return (
            "Mount:\n"
            f"    Physical Type:     {OpticalToolbox.mount_physical_type_to_text(self.get_physical_type())}\n"
            f"    Motion Type:       {OpticalToolbox.mount_motion_type_to_text(self.get_motion_type())}\n"
            f"    Mount Plate Type:  {OpticalToolbox.mount_plate_type_to_text(self.get_mount_plate_type())}\n"
            f"    Mount Weight Rating: {self.get_weight_rating()}kg maximum\n"
            f"    Mount is GOTO:     {'Yes' if self.has_computerized_goto() else 'No'}"
        )
