# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025

"""
This abstract class represents reflecting telescopes. Newtonian OTAs inherit from this class.
"""

from OTA import OTA

class Reflector(OTA):
    def __init__(self, ota_type, aperture, focal_length, mount_plate_type, weight):
        super().__init__(ota_type, aperture, focal_length, mount_plate_type, weight)
