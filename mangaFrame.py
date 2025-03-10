from renameLogic import *
from tkinter import Label, Entry, font


class MangaFrame(tkinter.Frame):

    def __init__(self):
        super().__init__()
        padding = {"padx" : 5, "pady" : 5}

        name_label = Label(self, text="Manga name: ")
        name_label.grid(row=0, column=0, **padding, sticky="w")

        name_entry = Entry(self)
        name_entry.grid(row=0, column=1, **padding, sticky="w")

        directory_label = Label(self, text="Folder directory:")
        directory_label.grid(row=1, column=0, **padding, sticky="w")

        current_directory = tkinter.StringVar()
        current_directory.set("")
        directory_entry = Entry(self, textvariable=current_directory, justify="left", width=50,
                                font=font.Font(slant=font.ITALIC, weight=font.NORMAL, size=10))
        directory_entry.grid(row=1, column=1, **padding, sticky="w")

        directory_button = tkinter.Button(self, text="Select directory", command= lambda : select_directory(current_directory))
        directory_button.grid(row=1, column=2, **padding, sticky="w")

        rename_files_button = tkinter.Button(self, text="Rename files",
                                             command=lambda: rename_manga(current_directory.get(), name_entry.get()))
        rename_files_button.grid(row=2, column=1, **padding, sticky="ns")
