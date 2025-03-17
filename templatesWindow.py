import tkinter
import re
from tkinter import Listbox, Entry, Button, Label, Frame, StringVar



class TemplatesWindow(tkinter.Toplevel):

    def __init__(self):
        super().__init__()

        """
        Class variables
        """
        self.padding = {"padx": 10, "pady": 10}

        self.manga_template_frame = Frame(self)
        self.anime_template_frame = Frame(self)

        self.manga_template_list = ["Noragami", "Bungou Stray Dogs"]
        self.anime_template_list = ["Chainsaw Man", "Vanitas no Carte"]

        self.manga_listbox_items = StringVar(value= self.manga_template_list)

        self.anime_listbox_items = StringVar(value= self.anime_template_list)

        self.new_anime_template = StringVar()
        self.new_manga_template = StringVar()



        self.title("Templates configuration")
        self.focus()
        self.grab_set()
        self.config(background= "white")

        self.fill_manga_frame()
        self.fill_anime_frame()

        self.manga_template_frame.pack(side = "left", padx = 20, pady = 20)
        self.anime_template_frame.pack(side = "right", padx = 20, pady = 20)


    def is_manga_template_correct(self) -> bool:
        return True

    def is_anime_template_correct(self) -> bool:
        #TODO: check if the new anime template contains the necessary fields
        return True

    def fill_template_lists(self):
        #TODO: read templates from database and fill lists with the data
        pass

    def delete_anime_template(self):
        # TODO: delete the selected anime template from the list
        # TODO: delete the selected anime template from the DB
        pass

    def delete_manga_template(self):
        #TODO: delete the selected manga template from the list
        #TODO: delete the selected manga template from the DB
        pass

    def add_manga_template(self):
        if self.is_manga_template_correct():
            self.manga_template_list.append(self.new_manga_template.get())
            self.manga_listbox_items.set(self.manga_template_list)
            #TODO: add the new template to the DB

            self.new_manga_template.set("")
        pass

    def add_anime_template(self):
        if self.is_anime_template_correct():
            self.anime_template_list.append(self.new_anime_template.get())
            self.anime_listbox_items.set(self.anime_template_list)
            # TODO: add the new template to the DB

            self.new_anime_template.set("")
        pass

    def fill_manga_frame(self):
        """
        Sets the necessary elements inside the manga frame
        """
        manga_label = Label(self.manga_template_frame, text="MANGA TEMPLATES")
        manga_label.grid(row=0, column=0, columnspan=2, **self.padding)

        manga_template_listbox = Listbox(self.manga_template_frame, listvariable= self.manga_listbox_items)
        manga_template_listbox.grid(row=1, column=0, **self.padding, sticky="we")

        delete_manga_button = Button(self.manga_template_frame, text="Delete selected")
        delete_manga_button.grid(row=1, column=1, padx=(0, 10))

        manga_entry = Entry(self.manga_template_frame, textvariable= self.new_manga_template, width=50)
        manga_entry.grid(row=2, column=0, **self.padding)

        add_manga_button = Button(self.manga_template_frame, text="Add template",
                                  command= self.add_manga_template)
        add_manga_button.grid(row=2, column=1, padx=(0, 10))


    def fill_anime_frame(self):
        """
        Sets the necessary elements inside the anime frame
        :return:
        """
        anime_label = Label(self.anime_template_frame, text="ANIME TEMPLATES")
        anime_label.grid(row=0, column=2, columnspan=2, **self.padding)

        anime_template_listbox = Listbox(self.anime_template_frame, listvariable= self.anime_listbox_items)
        anime_template_listbox.grid(row=1, column=2, **self.padding, sticky="we")

        delete_anime_button = Button(self.anime_template_frame, text="Delete selected")
        delete_anime_button.grid(row=1, column=3, padx=(0, 10))

        anime_entry = Entry(self.anime_template_frame, textvariable=self.new_anime_template, width=50)
        anime_entry.grid(row=2, column=2, **self.padding)

        add_anime_button = Button(self.anime_template_frame, text="Add template",
                                  command= self.add_anime_template)
        add_anime_button.grid(row=2, column=3, padx=(0, 10))

    def center_window(self: tkinter.Toplevel):
        #TODO: center window in screen
        pass