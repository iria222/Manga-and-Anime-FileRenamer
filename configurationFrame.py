import tkinter
from tkinter import Label, Entry, Button


class ConfigurationFrame(tkinter.Frame):

    def __init__(self):
        super().__init__()
        padding = {"padx": 5, "pady": 5}


        manga_label = Label(self, text= "Manga template")
        manga_label.grid(row = 0, column = 0, **padding, sticky = "w")

        manga_entry = Entry(self, width = 50)
        manga_entry.grid(row = 0, column = 1, **padding, sticky = "w")

        save_manga_button = Button(self, text= "Save")
        save_manga_button.grid(row = 0, column = 2, **padding, sticky = "w")

        anime_label = Label(self, text="Anime template")
        anime_label.grid(row=1, column=0, **padding, sticky="w")

        anime_entry = Entry(self, width = 50)
        anime_entry.grid(row=1, column=1, **padding, sticky="w")

        save_anime_button = Button(self, text="Save")
        save_anime_button.grid(row=1, column=2, **padding, sticky="w")
