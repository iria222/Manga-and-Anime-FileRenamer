import os
import tkinter
from functools import partial
from tkinter import filedialog, messagebox
from natsort import natsorted

default_anime_template = """{name} S{season_number:02d}E{current_number:02d}"""
default_manga_template = """{name} V{current_number:02d}"""

anime_template = default_anime_template
manga_template = default_manga_template

def set_manga_template(template):
    global manga_template
    manga_template = template

def set_anime_template(template):
    global anime_template
    anime_template = template

def select_directory(current_directory):
    """
    Sets the directory selected by the user as the current directory
    :param current_directory: folder route
    """
    directory_route = filedialog.askdirectory()
    if directory_route != "":
        directory_route += "/"
        current_directory.set(directory_route)


def rename_manga(folder_directory, name):
    """
    Renames a list of files using the manga template
    :param folder_directory: route of selected folder
    :param name: manga's name
    """
    if not can_be_renamed(folder_directory, name):
        return 1
    #template = template.format(name = name)
    template = partial(manga_template.format, name = name)
    rename_file(folder_directory, template)


def rename_anime(folder_directory, name, season):
    """
    Rename a list of files using the anime template
    :param folder_directory: route of selected folder
    :param name: anime's name
    :param season: season of the anime's episodes
    """
    season = int(season)
    #template = template.format(name = name, season_number = season)
    template = partial(anime_template.format, name = name, season_number = season)
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

        filled_template = template(current_number = current_number)
        destination = folder_directory + filled_template + "." + extension
        os.rename(source, destination)

        current_number += 1

    tkinter.messagebox.showinfo("Info", "The files have been renamed")

def can_be_renamed(folder_directory, name) -> bool:
    """
    Checks if a list of files can be renamed
    :param folder_directory: path of the selected folder
    :param name: name of the anime/manga
    :return: can or cannot be renamed
    """
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