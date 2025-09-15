# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025

"""
This class represents a Galilean (Refractor) OTA. It inherits from the Refractor
class, which itself inherits from OTA.

"""
from Refractor import Refractor

class Galilean(Refractor):
    def __init__(self, aperture, focal_length, mount_plate_type, weight):
        super().__init__('G', aperture, focal_length, mount_plate_type, weight)
