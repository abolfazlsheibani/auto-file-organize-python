
# 📂 Auto File Organizer

A smart Python script that automatically organizes your **Downloads** folder by moving files into categorized folders based on their file extensions.

## ✨ Features
- **Automatic Categorization:** Sorts files into folders like Images, Documents, Videos, Audio, Programs, and Archives.
- **Dynamic Pathing:** Automatically detects the current user's home directory, making it work on any Windows machine.
- **Safe File Handling:** Prevents overwriting files by automatically renaming duplicates (e.g., `photo(1).jpg`).
- **Catch-all Folder:** Any unknown file types are neatly moved to an `Others` folder.

## 🚀 How it Works
The script scans the `Downloads` folder, checks the extension of each file, and moves it to the corresponding folder. If the destination folder doesn't exist, the script creates it automatically.

## 🛠️ Technologies Used
- **Language:** Python 3
- **Modules:** `os`, `shutil`

## 💻 How to Use
1. Clone this repository or download the `file_organizer.py` file.
2. Run the script using Python:
   ```bash
   python file_organizer.py
   ```
3. Check your Downloads folder and enjoy the organization!

---
*Developed as a part of my Python learning journey to automate daily tasks.* 🚀
```
