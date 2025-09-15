#Name: Yosef Mekonnen
#Assignment: AS4
# 01-07-2025

"""
This is a utility class with static helper methods used throughout the program.
It provides things like mount plate type translation, magnification calculations,
and field-of-view math.
"""

class OpticalToolbox(object):

    @staticmethod
    def effective_magnification(ota, ep):
        mag = ota.get_focal_length() / ep.get_focal_length()
        if mag == int(mag):
            return int(mag)
        else:
            return round(mag, 1)

    @staticmethod
    def f_ratio(ota):
        ratio = ota.get_focal_length() / ota.get_aperture()
        if ratio == int(ratio):
            return int(ratio)
        else:
            return round(ratio, 1)

    @staticmethod
    def eyepiece_usability(ota, ep):
        mag = OpticalToolbox.effective_magnification(ota, ep)
        return mag <= 2 * ota.get_aperture()

    @staticmethod
    def true_fov(ota, ep):
        mag = OpticalToolbox.effective_magnification(ota, ep)
        tfov = ep.get_afov() / mag
        if tfov == int(tfov):
            return int(tfov)
        else:
            return round(tfov, 1)

    @staticmethod
    def mount_plate_type_to_text(code):
        # Turn mount plate code into full text
        if code == "NA":
            return "Not Applicable - Dobsonian"
        elif code == "V":
            return "Vixen 1.75\""
        elif code == "D":
            return "Losmandy 3\""
        else:
            return "Unknown"

    @staticmethod
    def mount_physical_type_to_text(code):
        if code == "T":
            return "Tripod"
        elif code == "D":
            return "Dobsonian"
        else:
            return "Unknown"

    @staticmethod
    def mount_motion_type_to_text(code):
        if code == "AA":
            return "Altitude-Azimuth"
        elif code == "EQ":
            return "Equatorial"
        else:
            return "Unknown"

    @staticmethod
    def ota_type_to_text(code):
        ota_dict = {
            "G": "Galilean (Refractor)",
            "N": "Newtonian (Reflector)",
            "S": "Schmidt-Cassegrain (Catadioptric)",
            "M": "Maksutov-Cassegrain (Catadioptric)"
        }
        return ota_dict.get(code, "Unknown")
