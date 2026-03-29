import os
import json
import shutil

HISTORY_FILE = "history.json"


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def record_move(source, destination):
    history = load_history()
    history.append({
        "source": source,
        "destination": destination
    })
    save_history(history)


def remove_empty_folder(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        if not os.listdir(folder_path):
            os.rmdir(folder_path)


def undo_last_organization():
    history = load_history()

    if not history:
        return False

    for entry in reversed(history):
        source = entry["source"]
        destination = entry["destination"]

        if os.path.exists(destination):
            os.makedirs(os.path.dirname(source), exist_ok=True)
            shutil.move(destination, source)

            destination_folder = os.path.dirname(destination)
            remove_empty_folder(destination_folder)

    save_history([])
    return True