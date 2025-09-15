#Name: Yosef Mekonnen
#Assignment: AS4
# 01-07-2025

"""
This file defines the abstract base class OTA (Optical Tube Assembly). It stores
shared attributes like type, aperture, focal length, mount plate type,
and weight. Child classes like Newtonian or SchmidtCassegrain inherit from this.

"""

from OpticalToolbox import OpticalToolbox

class OTA(OpticalToolbox):
    def __init__(self, type, aperture, focal_length , mount_plate_type, weight):
        self.__type = type
        self.__aperture = aperture
        self.__focal_length = focal_length
        self.__mount_plate_type = mount_plate_type
        self.__weight = weight

    def get_type(self):
        return self.__type

    def get_aperture(self):
        return self.__aperture

    def get_focal_length(self):
        return self.__focal_length

    def get_mount_plate_type(self):
        return self.__mount_plate_type

    def get_weight(self):
        return self.__weight

    def __str__(self):
        full_type = OpticalToolbox.ota_type_to_text(self.get_type())
        return (
            "OTA\n"
            f"    Type:           {full_type}\n"
            f"    Aperture:       {self.get_aperture()}mm\n"
            f"    Focal Length:   {self.get_focal_length()}mm\n"
            f"    Mount Plate Type: {OpticalToolbox.mount_plate_type_to_text(self.get_mount_plate_type())}\n"
            f"    OTA Weight:     {self.get_weight()}kg"
        )
