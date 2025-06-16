import os
import tkinter
from functools import partial
from tkinter import filedialog, messagebox
from natsort import natsorted

import Data.globalData as globalData


def select_directory(current_directory):
    """
    Sets the passed path as the current directory
    :param current_directory: folder path
    """
    directory_path = filedialog.askdirectory()
    if directory_path != "":
        directory_path += "/"
        current_directory.set(directory_path)


def rename_manga(folder_directory, name, starter_number = 1):
    """
    Renames a list of files using the manga template
    :param starter_number: number to assign to the first file
    :param folder_directory: path of the folder where the files are stored
    :param name: manga's name
    """
    aux_manga_template = globalData.manga_template.replace("{volume_number", "{current_number")
    template = partial(aux_manga_template.format, name = name)
    rename_files(folder_directory, template, starter_number)

def rename_anime(folder_directory, name, season = 1, starter_number = 1):
    """
    Rename a list of files using the anime template
    :param starter_number: number to assign to the first file
    :param folder_directory: path of the folder where the files are stored
    :param name: anime's name
    :param season: season of the anime's episodes
    """
    aux_anime_template = globalData.anime_template.replace("{episode_number", "{current_number")

    if "{season_number" in globalData.anime_template:
        template = partial(aux_anime_template.format, name = name, season_number = season)
    else:
        template = partial(aux_anime_template.format, name = name)
    rename_files(folder_directory, template, starter_number)


def rename_files(folder_directory, template, starter_number):
    """
    Renames the files of the passed directory
    :param starter_number: number to assign to the first file
    :param folder_directory: path of the folder in which the files are stored
    :param template: template to follow when renaming the files
    """
    current_number = starter_number
    #Get a list of the files' names excluding the directories
    file_list = natsorted([f.name for f in os.scandir(folder_directory) if f.is_file(follow_symlinks=False)])

    try:
        for file in file_list:
            source = folder_directory + file
            extension = file.split(".")
            extension = extension[len(extension) - 1]

            filled_template = template(current_number = current_number)
            destination = folder_directory + filled_template + "." + extension

            os.rename(source, destination)

            current_number += 1

    except FileExistsError as error:
        tkinter.messagebox.showerror("Error", f"Error occurred when renaming the files - {error}")
    else:
        tkinter.messagebox.showinfo("Info", "The files have been renamed")