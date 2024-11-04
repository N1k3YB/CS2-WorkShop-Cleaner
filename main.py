import os
import re
import shutil
import tkinter as tk
from tkinter import messagebox, Listbox, Checkbutton, BooleanVar

def extract_title_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    title_match = re.search(r'"title"\s+"(.*?)"', content)
    return title_match.group(1) if title_match else None

def find_publish_data(base_folder):
    folders_with_titles = []

    for root, _, files in os.walk(base_folder):
        if 'publish_data.txt' in files:
            file_path = os.path.join(root, 'publish_data.txt')
            title = extract_title_from_file(file_path)
            if title:
                folder_name = os.path.basename(root)
                folders_with_titles.append((folder_name, title, root))
    
    return folders_with_titles

def delete_selected_folders():
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("Удаление", "Пожалуйста, выберите хотя бы одну папку для удаления.")
        return

    confirmed = messagebox.askyesno("Подтверждение удаления", "Вы уверены, что хотите удалить выбранные папки?")
    if not confirmed:
        return

    for idx in selected_indices:
        folder_info = folders[idx]
        folder_path = folder_info[2]
        try:
            shutil.rmtree(folder_path)
            listbox.delete(idx)
            print(f"Папка '{folder_info[0]}' успешно удалена.")
        except Exception as e:
            messagebox.showerror("Ошибка удаления", f"Не удалось удалить папку '{folder_info[0]}': {e}")

def create_gui(folders):
    global listbox

    root = tk.Tk()
    root.title("CS2 WSC")

    tk.Label(root, text="Список папок с title:").pack()

    listbox = Listbox(root, selectmode=tk.MULTIPLE, width=50, height=20)
    for folder_name, title, _ in folders:
        listbox.insert(tk.END, f"{folder_name}: {title}")
    listbox.pack()

    delete_button = tk.Button(root, text="Удалить выбранные папки", command=delete_selected_folders)
    delete_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    base_folder = os.path.dirname(os.path.abspath(__file__)) 
    folders = find_publish_data(base_folder)

    if folders:
        create_gui(folders)
    else:
        print("Не найдено папок с файлом publish_data.txt.")
