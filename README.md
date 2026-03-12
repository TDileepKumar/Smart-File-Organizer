# Smart-File-Organizer

A Python automation tool that organizes files based on file type and detects duplicate files.

## Features

- Automatic file categorization
- Folder creation
- Duplicate file detection
- File organization automation

## Technologies

- Python
- OS module
- hashlib
- shutil

## Project Structure

Smart-File-Organizer/
│
├── organizer.py        # Main script
├── utils.py            # Helper functions
├── config.py           # File type categories
├── README.md
├── requirements.txt
└── .gitignore

## Architecture

Input Folder
     │
     ▼
organizer.py
     │
     ├── utils.get_file_hash()
     ├── utils.get_category()
     └── utils.move_file()
     │
     ▼
Categorized Folders
(Images / Documents / Code / Others)

## Example

Before:

Downloads/
    photo.jpg
    report.pdf
    script.py

After running:

Downloads/
    Images/
        photo.jpg
    Documents/
        report.pdf
    Code/
        script.py

## How to Run

```bash
python organizer.py --path "Folder_location"
