# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025

"""
This class represents a telescope package containing an OTA, a mount, and one or more eyepieces.
It provides methods to add components, retrieve them, generate formatted output,
and now includes support for sorting and searching based on OTA type, mount type, or package number.
"""

class Package:
    counter = 1
    sort_key = "number"  # Default sort key

    def __init__(self):
        self.__ota = None
        self.__mount = None
        self.__eps = []
        self.__number = Package.counter
        Package.counter += 1

    def set_ota(self, ota):
        self.__ota = ota

    def set_mount(self, mount):
        self.__mount = mount

    def add_ep(self, ep):
        self.__eps.append(ep)

    def get_number(self):
        return self.__number

    def get_eps(self):
        return self.__eps

    def get_ota(self):
        return self.__ota

    def get_mount(self):
        return self.__mount

    def __str__(self):
        output = f"***** PACKAGE {self.get_number()} *****\n"
        if self.__ota is not None:
            output += str(self.__ota) + "\n"
        if self.__mount is not None:
            output += str(self.__mount) + "\n"
        for ep in self.__eps:
            output += str(ep) + "\n"
        output += "=" * 40
        return output

    @staticmethod
    def sort_by_number():
        Package.sort_key = "number"

    @staticmethod
    def sort_by_ota():
        Package.sort_key = "ota"

    @staticmethod
    def sort_by_mount():
        Package.sort_key = "mount"

    def get_sort_key(self):
        if Package.sort_key == "number":
            return self.get_number()
        elif Package.sort_key == "ota":
            return self.__ota.get_type() if self.__ota else ""
        elif Package.sort_key == "mount":
            return self.__mount.get_physical_type() if self.__mount else ""
        else:
            return self.get_number()

    def __lt__(self, other):
        if not isinstance(other, Package):
            return NotImplemented
        return self.get_sort_key() < other.get_sort_key()
