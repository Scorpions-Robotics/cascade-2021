import cv2

import os, glob

from os import listdir, makedirs

from os.path import isfile, join

path_p = input("Current path: ")

dstpath_p = input("Destination path: ")

path = r"{}".format(path_p)  # Source Folder
dstpath = r"{}".format(dstpath_p)  # Destination Folder

try:
    makedirs(dstpath)

except Exception as e:
    print("Directory already exist, images will be written in same folder")
    print(e)
# Folder won't used
files = list(filter(lambda f: isfile(join(path, f)), listdir(path)))

for image in files:
    try:
        img = cv2.imread(os.path.join(path, image))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dstPath = join(dstpath, image)
        cv2.imwrite(dstPath, gray)
    except Exception as e:
        print("{} is not converted".format(image))
        print(e)

for fil in glob.glob("*.jpg"):
    try:
        image = cv2.imread(fil)
        gray_image = cv2.cvtColor(
            os.path.join(path, image), cv2.COLOR_BGR2GRAY
        )  # convert to greyscale
        cv2.imwrite(os.path.join(dstpath, fil), gray_image)
    except Exception as e:
        print("{} is not converted")
        print(e)
