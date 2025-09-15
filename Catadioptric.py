# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025

"""
This abstract class represents catadioptric OTAs. It is a subclass of OTA and
is inherited by concrete types like Schmidt-Cassegrain and Maksutov-Cassegrain.
"""

from OTA import OTA

class Catadioptric(OTA):
    def __init__(self, ota_type, aperture, focal_length, mount_plate_type, weight):
        super().__init__(ota_type, aperture, focal_length, mount_plate_type, weight)
