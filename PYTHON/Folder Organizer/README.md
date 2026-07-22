
# Create a Markdown file content for the README
readme_content = 📦 Downloads Folder Organizer

An automated Python script designed to organize messy download folders into neatly categorized subdirectories based on file extensions.

---

## 📌 Project Overview

It is common for the `Downloads` directory to get cluttered over time with documents, images, installers, and compressed files. This utility automatically scans the folder, detects each file's extension, and moves it to its designated directory. Any unrecognized file formats are safely routed to an `Others` folder.

---

## ✨ Features

- **Automatic Extension Detection:** Categorizes files into `Images`, `Documents`, `Executables`, `Compressed`, `Audio/Video`, etc.
- **Catch-All Management (`Others` folder):** Ensures no file is left behind or misplaced.
- **Directory Auto-Creation:** Dynamically creates target subfolders only when needed.
- **Safe Execution:** Skips existing directories to avoid nested folder moves or accidental corruption.

---

## 🛠️ Project Structure

Saída de código
README.md generated successfully.

```text
Folder Organizer/
├── Organizer.py          # Main automation script
└── README.md          # Project documentation
