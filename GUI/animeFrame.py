from tkinter import Label, Entry, font, messagebox
from entryWithPlaceholder import EntryWithPlaceholder
from renameLogic import *

class AnimeFrame(tkinter.Frame):

    def __init__(self):
        super().__init__()

        padding = {"padx": 5, "pady": 5}
        self.bind_all("<Button-1>", lambda event: event.widget.focus_set())

        name_label = Label(self, text="Anime name: ")
        name_label.grid(row=0, column=0, **padding, sticky="w")

        name_entry = Entry(self)
        name_entry.grid(row=0, column=1, **padding, sticky="w")

        starter_number_label = Label(self, text = "Starter number: ")
        starter_number_label.grid(row = 1, column = 0, **padding, sticky="w")

        starter_number_entry = EntryWithPlaceholder(self, "1")
        starter_number_entry.grid(row = 1, column = 1, **padding, sticky = "w")

        season_label = Label(self, text = "Season number: ")
        season_label.grid(row = 2, column = 0, **padding, sticky="w")

        season_entry = EntryWithPlaceholder(self, "1")
        season_entry.grid(row = 2, column = 1, **padding, sticky="w")

        directory_label = Label(self, text="Folder directory:")
        directory_label.grid(row=3, column=0, **padding, sticky="w")

        current_directory = tkinter.StringVar()
        current_directory.set("")
        directory_entry = Entry(self, textvariable=current_directory, justify="left", width=50,
                                font=font.Font(slant=font.ITALIC, weight=font.NORMAL, size=10))
        directory_entry.grid(row=3, column=1, **padding, sticky="w")

        directory_button = tkinter.Button(self, text="Select directory",
                                          command=lambda: select_directory(current_directory))
        directory_button.grid(row=3, column=2, **padding, sticky="w")

        rename_files_button = tkinter.Button(self, text="Rename files",
                                             command=lambda: AnimeFrame.rename_files(name_entry.get(), directory_entry.get(),
                                                                                     season_entry.get(), starter_number_entry.get()))
        rename_files_button.grid(row=4, column=1, **padding, sticky="ns")



    @staticmethod
    def rename_files(name, folder_directory, season, starter_number):
        """
        Rename files inside a folder
        :param starter_number: number to assign to the first file
        :param name: anime's name
        :param folder_directory: path of the selected folder
        :param season: anime's season
        :return: function to call to rename files
        """
        if AnimeFrame.check_fields(name, folder_directory, season, starter_number):
            return rename_anime(folder_directory, name, int(season), int(starter_number))
        else:
            return 1

    @staticmethod
    def check_fields(name, folder_directory, season, starter_number) -> bool:
        """
        Check if the gui fields are filled correctly
        :param starter_number: number to assign to the first file
        :param name: anime's name
        :param folder_directory: path of the selected folder
        :param season: anime's season
        :return: True if fields are filled correctly or not
                 False if not
        """
        if name == "":
            tkinter.messagebox.showerror("Error", "Name field can't be empty")
            return False

        if not starter_number.isdigit():
            tkinter.messagebox.showerror("Error", "Starter number must be a positive integer number")
            return False

        if not season.isdigit():
            tkinter.messagebox.showerror("Error", "Season must be a positive integer number")
            return False

        if folder_directory == "":
            tkinter.messagebox.showerror("Error", "Folder directory can't be empty")
            return False

        if not (os.path.exists(folder_directory) and os.path.isdir(folder_directory)):
            tkinter.messagebox.showerror("Error", "Folder directory is not valid")
            return False

        return True
