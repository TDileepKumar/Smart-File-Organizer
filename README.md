# Smart-File-Organizer

A Python automation tool that organizes files in a folder based on file type and detects duplicate files using file hashing.

## Features

- Automatic file categorization
- Folder creation
- Duplicate file detection
- File organization automation

## Technologies Used

- Python
- os module
- hashlib
- shutil
- argparse
- logging

## Project Structure

	Smart-File-Organizer/
	│
	├── organizer.py       # Main program
	├── utils.py           # Helper functions
	├── config.py          # File category configuration
	├── README.md
	├── requirements.txt
	└── .gitignore

## Installation

Clone the repository

	git clone https://github.com/TDileepKumar/Smart-File-Organizer.git

Navigate to the folder

	cd Smart-File-Organizer

## Usage

Run the script using:

	python organizer.py --path "Folder_Location"

#### Example:

	python organizer.py --path "C:\Users\User\Downloads"

## Example

Before Organizing:

	Downloads/
		photo.jpg	
		report.pdf	
		script.py

After Organizing:

	Downloads/
		Images/    
			photo.jpg	   
		Documents/    
			report.pdf	   
		Code/    
			script.py

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


## Demo
Before Organizing:

![Before](Screenshots/Before.png)

After Organizing:

![After](Screenshots/After.png)
