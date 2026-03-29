import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import threading
from organizer import organize_folder
from undo_manager import undo_last_organization

root = tk.Tk()
root.title("Smart File Organizer")
root.geometry("550x500")


title = tk.Label(root, text="Smart File Organizer", font=("Arial", 16))
title.pack(pady=10)


path_label = tk.Label(root, text="No folder selected")
path_label.pack()


status_label = tk.Label(root, text="")
status_label.pack()


log_box = scrolledtext.ScrolledText(root, width=60, height=12)
log_box.pack(pady=10)


progress = ttk.Progressbar(root, orient="horizontal", length=420, mode="determinate")
progress.pack(pady=10)


def log_message(message):
    log_box.insert(tk.END, message + "\n")
    log_box.see(tk.END)


def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        path_label.config(text=folder_path)


def update_progress(current, total):
    if total == 0:
        progress["value"] = 0
        return

    percent = (current / total) * 100
    progress["value"] = percent
    root.update_idletasks()


def run_organizer(folder):
    organize_folder(folder, log_message, update_progress)
    status_label.config(text="Organization completed")
    start_btn.config(state=tk.NORMAL)


def start_organizing():
    folder = path_label.cget("text")

    if folder != "No folder selected":
        progress["value"] = 0
        status_label.config(text="Organizing files...")
        start_btn.config(state=tk.DISABLED)

        thread = threading.Thread(target=run_organizer, args=(folder,))
        thread.start()


def undo_action():
    success = undo_last_organization()

    if success:
        log_message("Undo completed successfully")
        status_label.config(text="Last organization undone")
        progress["value"] = 0
    else:
        log_message("No history found to undo")
        status_label.config(text="Nothing to undo")


browse_btn = tk.Button(root, text="Select Folder", command=select_folder)
browse_btn.pack(pady=10)


start_btn = tk.Button(root, text="Organize Files", command=start_organizing)
start_btn.pack(pady=10)


undo_btn = tk.Button(root, text="Undo", command=undo_action)
undo_btn.pack(pady=5)


root.mainloop()