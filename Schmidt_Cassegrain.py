# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025

"""
This class defines a Schmidt-Cassegrain OTA. It inherits from the Catadioptric
class, which is a subclass of OTA.
"""

from Catadioptric import Catadioptric

class SchmidtCassegrain(Catadioptric):
    def __init__(self, aperture, focal_length, mount_plate_type, weight):
        super().__init__('S', aperture, focal_length, mount_plate_type, weight)
