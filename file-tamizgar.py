import os
import shutil

# پیدا کردن مسیر دانلودها به صورت خودکار
home_dir = os.path.expanduser("~")
downloads_path = os.path.join(home_dir, "Downloads")

# نقشه‌ی دسته‌بندی پسوندها
extension_to_folder = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images",
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents", ".pptx": "Documents",
    ".mp4": "Videos", ".mkv": "Videos", ".mov": "Videos",
    ".mp3": "Audio", ".wav": "Audio",
    ".exe": "Programs", ".msi": "Programs",
    ".zip": "Archives", ".rar": "Archives", ".7z": "Archives"
}

# بررسی فایل‌های موجود در پوشه دانلود
for filename in os.listdir(downloads_path):
    file_full_path = os.path.join(downloads_path, filename)
    
    # فقط روی فایل‌ها کار می‌کنیم
    if os.path.isfile(file_full_path):
        name, extension = os.path.splitext(filename)
        extension = extension.lower()
        
        # تعیین پوشه مقصد
        if extension in extension_to_folder:
            folder_name = extension_to_folder[extension]
        else:
            folder_name = "Others"
        
        folder_full_path = os.path.join(downloads_path, folder_name)
        
        if not os.path.exists(folder_full_path):
            os.makedirs(folder_full_path)
        
        # مدیریت فایل‌های تکراری برای جلوگیری از پاک شدن
        destination = os.path.join(folder_full_path, filename)
        counter = 1
        while os.path.exists(destination):
            new_name = f"{name}({counter}){extension}"
            destination = os.path.join(folder_full_path, new_name)
            counter += 1
        
        # جابه‌جایی فایل
        shutil.move(file_full_path, destination)
        print(f"Moved: {filename} -> {folder_name}")

print("\nDone! Everything is organized. ✨")
