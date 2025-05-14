import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Define the file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".java", ".cpp"]
}

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_category(file_extension):
    for category, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

def organize_directory(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            _, extension = os.path.splitext(item)
            category = get_category(extension)
            category_folder = os.path.join(path, category)
            create_folder_if_not_exists(category_folder)
            new_location = os.path.join(category_folder, item)
            shutil.move(item_path, new_location)

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_var.set(folder_selected)

def start_organizing():
    path = folder_path_var.get()
    if os.path.exists(path):
        organize_directory(path)
        messagebox.showinfo("Success", "Files organized successfully!")
    else:
        messagebox.showerror("Error", "The selected path does not exist.")

# Create the GUI
root = tk.Tk()
root.title("File Organizer")
root.geometry("500x180")
root.resizable(False, False)

folder_path_var = tk.StringVar()

tk.Label(root, text="Select Folder to Organize:", font=("Arial", 12)).pack(pady=10)
tk.Entry(root, textvariable=folder_path_var, width=50).pack(pady=5)
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)
tk.Button(root, text="Organize Files", command=start_organizing, bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=10)

root.mainloop()
