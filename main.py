
# Name: Yosef Mekonnen
# Assignment: AS4
# 01-07-2025

"""
This is the main driver program. It reads telescope, mount, and eyepiece data from text files,
builds packages using the appropriate classes, and demonstrates sorting and searching capabilities.
It supports selection sort on OTA type, mount type, or package number and binary search for
Maksutov-Cassegrain OTAs and Dobsonian mounts.
"""

from OTA import OTA
from Newtonian import Newtonian
from Galilean import Galilean
from Schmidt_Cassegrain import SchmidtCassegrain
from Maksutov_Cassegrain import MaksutovCassegrain
from Dobsonian import Dobsonian
from Tripod import Tripod
from Kellner import Kellner
from Plossl import Plossl
from Orthoscopic import Orthoscopic
from Nagler import Nagler
from Package import Package
from OpticalToolbox import OpticalToolbox
from Catadioptric import Catadioptric

packages = []

combo_list = [
    (8, 4, (17, 6)), (9, 4, (19, 4, 7)), (3, 2, (0, 16)), (4, 11, (12, 4, 15)),
    (1, 3, (16, 7)), (7, 8, (5,)), (14, 7, (11, 12, 7)), (14, 10, (17,)),
    (8, 8, (17, 5, 6)), (5, 11, (2, 4)), (12, 4, (0, 19, 13)), (11, 1, (10, 5)),
    (2, 16, (12, 5, 15)), (9, 6, (12, 6)), (11, 5, (5,)), (14, 1, (9, 18, 19)),
    (15, 8, (10, 13)), (7, 15, (4, 14)), (1, 17, (15,)), (8, 7, (18, 19, 5)),
    (3, 9, (12, 14)), (13, 7, (9, 4)), (13, 14, (5,)), (3, 0, (19, 15)),
    (7, 2, (0, 8)), (10, 19, (5,)), (13, 2, (8, 10, 6)), (3, 11, (19, 11, 4)),
    (15, 19, (8, 15)), (8, 13, (2, 15)), (0, 13, (19, 4, 7)), (7, 8, (18, 3, 14))
]

# Load data from files
otas = []
with open("otas.txt") as file:
    for line in file:
        if line.startswith("#") or not line.strip():
            continue
        parts = line.strip().split(",")
        type_code = parts[0].strip()
        ap = int(parts[1])
        fl = int(parts[2])
        plate = parts[3].strip()
        wt = float(parts[4])

        if type_code == "N":
            otas.append(Newtonian(ap, fl, plate, wt))
        elif type_code == "G":
            otas.append(Galilean(ap, fl, plate, wt))
        elif type_code == "S":
            otas.append(SchmidtCassegrain(ap, fl, plate, wt))
        elif type_code == "M":
            otas.append(MaksutovCassegrain(ap, fl, plate, wt))

nmounts = []
with open("mounts.txt") as file:
    for line in file:
        if line.startswith("#") or not line.strip():
            continue
        parts = line.strip().split(",")
        phy = parts[0].strip()
        mot = parts[1].strip()
        plate = parts[2].strip()
        weight = float(parts[3])
        goto = True if parts[4].strip().upper() == "Y" else False

        if phy == "D":
            nmounts.append(Dobsonian(mot, weight, goto))
        elif phy == "T":
            nmounts.append(Tripod(phy, mot, plate, weight, goto))

eps = []
with open("eps.txt") as file:
    for line in file:
        if line.startswith("#") or not line.strip():
            continue
        parts = line.strip().split(",")
        code = parts[0].strip()
        afov = int(parts[1])
        fl = int(parts[2])

        if code == "K":
            eps.append(Kellner(afov, fl))
        elif code == "P":
            eps.append(Plossl(afov, fl))
        elif code == "O":
            eps.append(Orthoscopic(afov, fl))
        elif code == "N":
            eps.append(Nagler(afov, fl))

for combo in combo_list:
    ota_idx, mount_idx, ep_indices = combo
    p = Package()
    p.set_ota(otas[ota_idx])
    p.set_mount(nmounts[mount_idx])
    for i in ep_indices:
        p.add_ep(eps[i])
    packages.append(p)

def selection_sort_packages(packages):
    for i in range(len(packages)):
        min_index = i
        for j in range(i + 1, len(packages)):
            if packages[j] < packages[min_index]:
                min_index = j
        packages[i], packages[min_index] = packages[min_index], packages[i]

def binary_search_packages(packages, target, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    mid_key = packages[mid].get_sort_key()
    if mid_key == target:
        return packages[mid]
    elif mid_key > target:
        return binary_search_packages(packages, target, low, mid - 1)
    else:
        return binary_search_packages(packages, target, mid + 1, high)

def print_sorted_packages(packages):
    print("IDX Package # OTA Type Physical Mount")
    print("=== ========= ======== ==============")
    for idx, p in enumerate(packages, start=1):
        ota_type = p.get_ota().get_type()
        mount_type = p.get_mount().get_physical_type()
        print(f"{idx:<3} {p.get_number():<9} {ota_type:<8} {mount_type:<14}")

# === SORT AND SEARCH STEPS ===
Package.sort_by_mount()
selection_sort_packages(packages)
print("\nSorting by Physical Mount Type")
print_sorted_packages(packages)

Package.sort_by_ota()
selection_sort_packages(packages)
print("\nSorting by OTA Type")
print_sorted_packages(packages)

Package.sort_by_number()
selection_sort_packages(packages)
print("\nSorting by Package Number")
print_sorted_packages(packages)

Package.sort_by_ota()
selection_sort_packages(packages)
result = binary_search_packages(packages, "M", 0, len(packages)-1)
print("\nBinary search: first instance of OTA Type Maksutov-Cassegrain")
if result:
    print(result)

Package.sort_by_mount()
selection_sort_packages(packages)
result = binary_search_packages(packages, "D", 0, len(packages)-1)
print("\nBinary search: first instance of Mount Type Dobsonian")
if result:
    print(result)
