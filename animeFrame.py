from tkinter import Label, Entry, font

from renameLogic import *

anime_template = """{name} S{season_number:02d}E{{current_number:02d}}"""
class AnimeFrame(tkinter.Frame):

    def __init__(self):
        super().__init__()

        padding = {"padx": 5, "pady": 5}

        name_label = Label(self, text="Anime name: ")
        name_label.grid(row=0, column=0, **padding, sticky="w")

        name_entry = Entry(self)
        name_entry.grid(row=0, column=1, **padding, sticky="w")

        season_label = Label(self, text = "Season number: ")
        season_label.grid(row = 1, column = 0, **padding, sticky="w")

        season_entry = Entry(self)
        season_entry.grid(row = 1, column = 1, **padding, sticky="w")

        directory_label = Label(self, text="Folder directory:")
        directory_label.grid(row=2, column=0, **padding, sticky="w")

        current_directory = tkinter.StringVar()
        current_directory.set("")
        directory_entry = Entry(self, textvariable=current_directory, justify="left", width=50,
                                font=font.Font(slant=font.ITALIC, weight=font.NORMAL, size=10))
        directory_entry.grid(row=2, column=1, **padding, sticky="w")

        directory_button = tkinter.Button(self, text="Select directory",
                                          command=lambda: select_directory(current_directory))
        directory_button.grid(row=2, column=2, **padding, sticky="w")

        rename_files_button = tkinter.Button(self, text="Rename files",
                                             command=lambda: rename_anime(current_directory.get(), name_entry.get(),
                                                                          season_entry.get(), anime_template))
        rename_files_button.grid(row=3, column=1, **padding, sticky="ns")
