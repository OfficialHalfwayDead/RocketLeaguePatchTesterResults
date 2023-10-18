import csv
import shutil
import os
import sys
import distutils
from distutils import dir_util

if len(sys.argv) != 2:
    print("Incorrect number of parameters provided")
    sys.exit()

patchnumber = str(sys.argv[1])

src = "C:/Program Files (x86)/Steam/steamapps/common/rocketleague/Binaries/Win64/bakkesmod/testmod"
dest = "E:/timoh/Documents/RLpatchTest/RocketLeaguePatchTesterResults/current_patch"
dest_numbered = os.path.join("E:/timoh/Documents/RLpatchTest/RocketLeaguePatchTesterResults", patchnumber)


def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f), 
                                    os.path.join(dest, f), 
                                    ignore)


recursive_overwrite(src, dest)

for path, dirs, files in os.walk(src):
    for filename in files:
        if 'current' in filename:
            continue
        if 'Emperor II' == filename: # for some reason this empty file without .csv keeps appearing
            continue
        fullpath = os.path.join(path, filename)
        semicolonin = csv.reader(open(fullpath, 'r', newline=''), delimiter=';')
        dest_fullpath = dest + "/" + path[len(src)+1:] + "/" + filename
        commaout = csv.writer(open(dest_fullpath, 'w', newline=''), delimiter=',')
        commaout.writerows(semicolonin)

distutils.dir_util.copy_tree(dest, dest_numbered)
