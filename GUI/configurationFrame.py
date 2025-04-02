import tkinter
from tkinter import Label, Button, StringVar
from tkinter.ttk import Combobox

from GUI.templatesWindow import TemplatesWindow
from DBManager import get_templates
from Data.globalData import TemplateType


class ConfigurationFrame(tkinter.Frame):

    def __init__(self):
        super().__init__()
        self.templates_window = None
        padding = {"padx": 5, "pady": 5}

        manga_label = Label(self, text= "Manga template")
        manga_label.grid(row = 0, column = 0, **padding, sticky = "w")

        self.manga_entry = Combobox(self, width = 50, values= get_templates(TemplateType.manga), state="readonly")
        self.manga_entry.grid(row = 0, column = 1, **padding, sticky = "w")

        anime_label = Label(self, text="Anime template")
        anime_label.grid(row=1, column=0, **padding, sticky="w")

        self.anime_entry = Combobox(self, width = 50, values= get_templates(TemplateType.anime), state="readonly")
        self.anime_entry.grid(row=1, column=1, **padding, sticky="w")

        open_temp_window_button = Button(self, text= "Edit templates",
                                         command= self.open_templates_window)
        open_temp_window_button.grid(row = 2, column = 1, **padding)

    def update_templates(self):
        """
        Updates the templates displayed in the comboboxes
        """
        self.manga_entry.config(values=get_templates(TemplateType.manga))
        self.anime_entry.config(values=get_templates(TemplateType.anime))

    def change_current_manga_template(self):
        #TODO: change the current manga template to the selected one
        pass

    def change_current_anime_template(self):
        #TODO: change the current anime template to the selected one
        pass

    def open_templates_window(self):
        self.templates_window = TemplatesWindow(self.update_templates)



