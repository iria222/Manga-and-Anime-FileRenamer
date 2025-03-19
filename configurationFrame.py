import re
import tkinter
from tkinter import Label, Button, messagebox
from tkinter.ttk import Combobox

from templatesWindow import TemplatesWindow


class ConfigurationFrame(tkinter.Frame):

    def __init__(self):
        super().__init__()
        self.templates_window = None
        padding = {"padx": 5, "pady": 5}


        manga_label = Label(self, text= "Manga template")
        manga_label.grid(row = 0, column = 0, **padding, sticky = "w")

        manga_entry = Combobox(self, width = 50)
        manga_entry.grid(row = 0, column = 1, **padding, sticky = "w")

        anime_label = Label(self, text="Anime template")
        anime_label.grid(row=1, column=0, **padding, sticky="w")

        anime_entry = Combobox(self, width = 50)
        anime_entry.grid(row=1, column=1, **padding, sticky="w")

        open_temp_window_button = Button(self, text= "Edit templates",
                                         command= self.open_templates_window)
        open_temp_window_button.grid(row = 2, column = 1, **padding)
        #TODO: change the current templates when the combobox selection is changed


    def open_templates_window(self):
        self.templates_window = TemplatesWindow()



