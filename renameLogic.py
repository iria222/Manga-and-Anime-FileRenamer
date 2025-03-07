import os
import tkinter
from tkinter import filedialog, messagebox
from natsort import natsorted

def select_directory(current_directory):
    directory_route = filedialog.askdirectory()
    if directory_route != "":
        directory_route += "/"
        current_directory.set(directory_route)


def rename_manga(folder_directory, name, template):
    if not can_be_renamed(folder_directory, name):
        return 1
    template = template.format(name = name)
    rename_file(folder_directory, template)


def rename_anime(folder_directory, name, season, template):
    if not can_be_renamed(folder_directory, name):
        return 1
    if season == "":
        tkinter.messagebox.showerror("Error", "Season field can't be empty")
        return 1
    if not season.isdigit():
        tkinter.messagebox.showerror("Error", "Season must be a positive integer number")
        return 1
    season = int(season)
    template = template.format(name = name, season_number = season)
    rename_file(folder_directory, template)


def rename_file(folder_directory, template):
    """
    Renames the files of the selected directory
    :param folder_directory: path of the folder in which the files are stored
    :param template: template to follow when renaming the files
    """
    current_number = 1
    file_list = natsorted(os.listdir(folder_directory))
    for file in file_list:
        source = folder_directory + file
        extension = file.split(".")
        extension = extension[len(extension) - 1]

        filled_template = template.format(current_number = current_number)
        destination = folder_directory + filled_template + "." + extension
        current_number += 1
        os.rename(source, destination)

    tkinter.messagebox.showinfo("Info", "The files have been renamed")

def can_be_renamed(folder_directory, name):
    if name == "":
        tkinter.messagebox.showerror("Error", "Name field can't be empty")
        return False

    if folder_directory == "":
        tkinter.messagebox.showerror("Error","Folder directory can't be empty")
        return False

    if not (os.path.exists(folder_directory) and os.path.isdir(folder_directory)):
        tkinter.messagebox.showerror("Error", "Folder directory is not valid")
        return False

    return True