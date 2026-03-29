import os
import shutil
import hashlib
from config import FILE_TYPES


def get_category(extension):
    extension = extension.lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Others"


def move_file(file_path, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    file_name = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, file_name)

    name, ext = os.path.splitext(file_name)
    counter = 1

    while os.path.exists(destination_path):
        new_name = f"{name}({counter}){ext}"
        destination_path = os.path.join(destination_folder, new_name)
        counter += 1

    shutil.move(file_path, destination_path)
    return destination_path


def get_file_hash(file_path):
    hasher = hashlib.md5()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()