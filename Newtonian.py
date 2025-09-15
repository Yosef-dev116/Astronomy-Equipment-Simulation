# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025
"""
This class represents a Newtonian Reflector OTA. It inherits from the Reflector
class, which itself inherits from OTA.

"""
from Reflector import Reflector

class Newtonian(Reflector):
    def __init__(self, aperture, focal_length, mount_plate_type, weight):
        super().__init__('N', aperture, focal_length, mount_plate_type, weight)
