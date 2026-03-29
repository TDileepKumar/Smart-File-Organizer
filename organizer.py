import os
import argparse
import logging
import shutil
from utils import get_category, move_file, get_file_hash
from undo_manager import record_move

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def organize_files(path):
    if not os.path.exists(path):
        print("Invalid path")
        return

    files = os.listdir(path)
    hashes = {}

    duplicate_folder = os.path.join(path, "duplicates")

    if not os.path.exists(duplicate_folder):
        os.makedirs(duplicate_folder)

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            file_hash = get_file_hash(file_path)

            if file_hash in hashes:
                print(f"Duplicate file found: {file}")
                logging.warning(f"Duplicate file detected: {file}")

                duplicate_destination = os.path.join(duplicate_folder, file)
                shutil.move(file_path, duplicate_destination)
                continue

            hashes[file_hash] = file

            filename, extension = os.path.splitext(file)

            category = get_category(extension)
            destination = os.path.join(path, category)

            logging.info(f"Moving {file} to {category}")
            move_file(file_path, destination)

    print("Files organized successfully.")


def organize_folder(path, logger=None, progress_callback=None):
    if not os.path.exists(path):
        return

    files = os.listdir(path)
    total_files = len(files)
    processed = 0

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            filename, extension = os.path.splitext(file)

            category = get_category(extension)
            destination = os.path.join(path, category)

            new_path = move_file(file_path, destination)
            record_move(file_path, new_path)

            if logger:
                logger(f"Moved {file} → {category}")

        processed += 1

        if progress_callback:
            progress_callback(processed, total_files)


def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer")

    parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="Folder path to organize"
    )

    args = parser.parse_args()

    organize_files(args.path)


if __name__ == "__main__":
    main()