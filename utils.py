import os
import shutil
from config import FILE_TYPES


def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def move_file(file_path, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    shutil.move(file_path, destination_folder)


import hashlib


def get_file_hash(file_path):
    hasher = hashlib.md5()

    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()