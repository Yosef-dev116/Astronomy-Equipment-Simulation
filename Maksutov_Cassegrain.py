# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025
"""
This class defines a Maksutov-Cassegrain OTA. Like SchmidtCassegrain, it
inherits from the Catadioptric base class.
"""

from Catadioptric import Catadioptric

class MaksutovCassegrain(Catadioptric):
    def __init__(self, aperture, focal_length, mount_plate_type, weight):
        super().__init__('M', aperture, focal_length, mount_plate_type, weight)
