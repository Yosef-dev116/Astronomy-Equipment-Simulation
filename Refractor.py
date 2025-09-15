# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025

"""
# This abstract class represents refracting telescopes.
# It inherits from OTA and is a parent of Galilean.

"""
from OTA import OTA

class Refractor(OTA):
    def __init__(self, ota_type, aperture, focal_length, mount_plate_type, weight):
        super().__init__(ota_type, aperture, focal_length, mount_plate_type, weight)
