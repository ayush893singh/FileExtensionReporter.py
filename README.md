# File Extension Reporter
File Extension Reporter is a simple Python utility that scans a folder and generates a report of the file extensions found inside it.

The program automatically counts files based on their extensions and displays the total number of files scanned.

# Features

- Scan files from a selected folder
- Detect file extensions automatically
- Count files by extension
- Scan files inside subfolders
- Display total number of files
- Handle invalid folder paths
- Simple command-line interface
- No external packages required

# Technologies Used

- Python 3
- "os" module
- "collections.Counter"
- File and directory handling
- Loops
- Conditional statements
- Exception handling

# How It Works

The program asks the user to enter a folder path.

It then scans the folder and its subfolders, detects the extension of each file, and counts how many files belong to each extension.

# For example:

.py     : 12 files
.jpg    : 7 files
.pdf    : 4 files
.txt    : 3 files

# FILE EXTENSION REPORTER


Enter folder path: /storage/emulated/0/Download
================
EXTENSION REPOR
================

.py : 12 files

----------------------------------------
Total Files : 12
=========

# How to Run

1. Clone the Repository

git clone YOUR_REPOSITORY_URL

2. Open the Project Folder

cd file-extension-reporter

3. Run the Program

python FileExtensionReporter.py

# Author
Ayush Singh https://github.com/ayush893singh/
