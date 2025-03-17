import tkinter
from tkinter import Listbox, Entry, Button, Label, Frame

from renameLogic import manga_template


class TemplatesWindow(tkinter.Toplevel):

    def __init__(self):
        super().__init__()
        self.title("Templates configuration")
        self.focus()
        self.grab_set()
        self.config(background= "white")

        padding = {"padx": 10, "pady": 10}

        self.manga_template_frame = Frame(self)
        self.anime_template_frame = Frame(self)

        manga_label = Label(self.manga_template_frame, text="MANGA TEMPLATES")
        manga_label.grid(row = 0, column = 0, columnspan = 2, **padding)

        manga_template_listbox = Listbox(self.manga_template_frame)
        manga_template_listbox.grid(row = 1, column = 0, **padding, sticky = "we")
        manga_template_listbox.insert(0, "Prueba manga")

        delete_manga_button = Button(self.manga_template_frame, text="Delete selected")
        delete_manga_button.grid(row = 1, column = 1, padx = (0, 10))

        manga_entry = Entry(self.manga_template_frame, width=50)
        manga_entry.grid(row=2, column=0, **padding)

        add_manga_button = Button(self.manga_template_frame, text= "Add template")
        add_manga_button.grid(row = 2, column = 1, padx = (0, 10))

        anime_label = Label(self.anime_template_frame, text = "ANIME TEMPLATES")
        anime_label.grid(row = 0, column = 2, columnspan = 2, **padding)

        anime_template_listbox = Listbox(self.anime_template_frame)
        anime_template_listbox.grid(row = 1, column = 2, **padding, sticky = "we")
        anime_template_listbox.insert(0, "Prueba anime")

        delete_anime_button = Button(self.anime_template_frame, text="Delete selected")
        delete_anime_button.grid(row=1, column=3, padx = (0, 10))

        anime_entry = Entry(self.anime_template_frame, width=50)
        anime_entry.grid(row=2, column=2, **padding)

        add_anime_button = Button(self.anime_template_frame, text = "Add template")
        add_anime_button.grid(row = 2, column = 3, padx = (0, 10))

        self.manga_template_frame.pack(side = "left", padx = 20, pady = 20)
        self.anime_template_frame.pack(side = "right", padx = 20, pady = 20)

    def center_window(self: tkinter.Toplevel):
        #TODO: center window in screen
        pass