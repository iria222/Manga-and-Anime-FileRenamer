import os
import tkinter
from functools import partial
from tkinter import filedialog, messagebox

from natsort import natsorted

default_anime_template = """{name} S{season_number:02d}E{episode_number:02d}"""
default_manga_template = """{name} V{volume_number:02d}"""

anime_template = default_anime_template
manga_template = default_manga_template

def set_manga_template(template):
    global manga_template
    manga_template = template

def get_manga_template():
    return manga_template

def set_anime_template(template):
    global anime_template
    anime_template = template

def get_anime_template():
    return anime_template

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
    #template = template.format(name = name)
    global manga_template
    aux_manga_template = manga_template.replace("{volume_number", "{current_number")
    template = partial(aux_manga_template.format, name = name)
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
    global anime_template
    aux_anime_template = anime_template.replace("{episode_number", "{current_number")
    template = partial(aux_anime_template.format, name = name, season_number = season)

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