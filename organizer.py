import os
from utils import get_category, move_file, get_file_hash

path = input("Enter folder path to organize: ")

if not os.path.exists(path):
    print("Invalid path")
    exit()

files = os.listdir(path)

hashes = {}

for file in files:

    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):

        file_hash = get_file_hash(file_path)

        if file_hash in hashes:
            print(f"Duplicate file found: {file}")
            continue

        hashes[file_hash] = file

        filename, extension = os.path.splitext(file)

        category = get_category(extension)

        destination = os.path.join(path, category)

        move_file(file_path, destination)

print("Files organized successfully.")