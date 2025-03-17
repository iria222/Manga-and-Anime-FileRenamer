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

    @staticmethod
    def check_anime_template(template) -> bool:
        """
        Check if the anime template is correct
        :param template: template to revise
        :return: True if template is correct
                 False if not
        """
        if not ConfigurationFrame.template_contains_name(template):
            tkinter.messagebox.showerror("Error", "Anime template must contain \"{name}\"")
            return False
        if not re.search(r'\{season(:\d\dd)?}', template):
            tkinter.messagebox.showerror("Error", "Anime template must contain \"{season}\"")
            return False
        return True

    @staticmethod
    def template_contains_name(template) -> bool:
        """
        Checks if a template contains the field {name}
        :param template: template to revise
        :return: True if contains {name}
                 False if not
        """
        if re.search(r'\{name}', template):
            return True
        else:
            return False

    @staticmethod
    def add_anime_template(template):
        """
        Adds a new template to the list of anime templates
        :param template: template to add
        """
        ConfigurationFrame.check_anime_template(template)
        #TODO: return the needed method from renameLogic to save the template

    @staticmethod
    def add_manga_template(template):
        """
        Adds a new template to the list of manga templates
        :param template: template to add
        """
        if not ConfigurationFrame.template_contains_name(template):
            tkinter.messagebox.showerror("Error", "Manga template must contain \"{name}\"")
            return 1
        # TODO: return the needed method from renameLogic to save the template