import tkinter
import re
from tkinter import Listbox, Entry, Button, Label, Frame, StringVar, messagebox
from DBManager import get_templates, insert_template, delete_template
from Data.globalData import TemplateType


class TemplatesWindow(tkinter.Toplevel):

    def __init__(self, update_func):
        super().__init__()

        """
        Class variables
        """
        self.padding = {"padx": 10, "pady": 10}

        self.manga_template_frame = Frame(self)
        self.anime_template_frame = Frame(self)

        self.manga_template_list = list(get_templates(TemplateType.manga)) #List that contains the manga templates
        self.anime_template_list = list(get_templates(TemplateType.anime)) #List that contains the anime templates

        self.manga_listbox = Listbox()
        self.anime_listbox = Listbox()

        self.manga_listbox_items = StringVar(value= self.manga_template_list)

        self.anime_listbox_items = StringVar(value= self.anime_template_list)

        self.new_anime_template = StringVar()
        self.new_manga_template = StringVar()



        self.title("Templates configuration")
        self.focus()
        self.grab_set()
        self.config(background= "white")
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(update_func))

        self.fill_manga_frame()
        self.fill_anime_frame()

        self.manga_template_frame.pack(side = "left", padx = 20, pady = 20)
        self.anime_template_frame.pack(side = "right", padx = 20, pady = 20)

    def on_closing(self, update_func):
        update_func()
        self.destroy()

    def is_manga_template_correct(self) -> bool:
        """
        Checks if the new manga template follows a correct pattern
        :return: True if it follows a correct pattern
                 False if not
        """
        template = self.new_manga_template.get()
        if not re.search(r'\{name}', template):
            messagebox.showerror("Error", "Manga template must contain \"{name}\"")
            return False

        if not re.search(r'\{volume_number(:\d\dd)?}', template):
            messagebox.showerror("Error", "Manga template must contain \"{volume_number}\"")
            return False

        return True

    def is_anime_template_correct(self) -> bool:
        """
        Checks if the new anime template follows a correct pattern
        :return: True if it follows a correct pattern
                 False if not
        """
        template = self.new_anime_template.get()
        if not re.search(r'\{name}', template):
            messagebox.showerror("Error", "Anime template must contain \"{name}\"")
            return False

        if "{season_number" in template and not re.search(r'\{season_number(:\d\dd)?}', template):
            messagebox.showerror("Error", "The format of the template is incorrect")
            return False

        if not re.search(r'\{episode_number(:\d\dd)?}', template):
            messagebox.showerror("Error", "Anime template must contain \"{episode_number}\"")
            return False

        return True

    def delete_anime_template(self):
        """
        Deletes the selected anime templates
        """
        selected_items = self.anime_listbox.curselection()
        if len(selected_items) > 0:
            for item in selected_items:
                if delete_template(self.anime_listbox.get(item), TemplateType.anime) == 1:
                    #The template could not be deleted
                    continue
                self.anime_template_list.remove(self.anime_listbox.get(item))

            self.anime_listbox_items.set(self.anime_template_list)

    def delete_manga_template(self):
        """
        Deletes the selected manga templates
        """
        selected_items = self.manga_listbox.curselection()
        if len(selected_items) > 0:
            for item in selected_items:
                if delete_template(self.manga_listbox.get(item), TemplateType.manga) == 1:
                    #The template could not be deleted
                    continue
                self.manga_template_list.remove(self.manga_listbox.get(item))
            self.manga_listbox_items.set(self.manga_template_list)

    def add_manga_template(self):
        """
        Inserts a new manga template
        """
        if not self.is_manga_template_correct():
            return 1

        if self.new_manga_template.get() in self.manga_template_list:
            messagebox.showerror("Error", "The template already exists")
            return 1

        self.manga_template_list.append(self.new_manga_template.get())
        self.manga_listbox_items.set(self.manga_template_list)
        insert_template(self.new_manga_template.get(), TemplateType.manga)
        self.new_manga_template.set("")
        return 0

    def add_anime_template(self):
        """
        Inserts a new anime template
        :return:
        """
        if not self.is_anime_template_correct():
            return 1

        if self.new_anime_template.get() in self.anime_template_list:
            messagebox.showerror("Error", "The template already exists")
            return 1

        self.anime_template_list.append(self.new_anime_template.get())
        self.anime_listbox_items.set(self.anime_template_list)
        insert_template(self.new_anime_template.get(), TemplateType.anime)
        self.new_anime_template.set("")
        return 0

    def fill_manga_frame(self):
        """
        Sets the necessary elements inside the manga frame
        """
        manga_label = Label(self.manga_template_frame, text="MANGA TEMPLATES")
        manga_label.grid(row=0, column=0, columnspan=2, **self.padding)

        self.manga_listbox = Listbox(self.manga_template_frame, listvariable= self.manga_listbox_items)
        self.manga_listbox.grid(row=1, column=0, **self.padding, sticky="we")

        delete_manga_button = Button(self.manga_template_frame, text="Delete selected",
                                     command= self.delete_manga_template)
        delete_manga_button.grid(row=1, column=1, padx=(0, 10))

        manga_entry = Entry(self.manga_template_frame, textvariable= self.new_manga_template, width=50)
        manga_entry.grid(row=2, column=0, **self.padding)

        add_manga_button = Button(self.manga_template_frame, text="Add template",
                                  command= self.add_manga_template)
        add_manga_button.grid(row=2, column=1, padx=(0, 10))

    def fill_anime_frame(self):
        """
        Sets the necessary elements inside the anime frame
        """
        anime_label = Label(self.anime_template_frame, text="ANIME TEMPLATES")
        anime_label.grid(row=0, column=2, columnspan=2, **self.padding)

        self.anime_listbox = Listbox(self.anime_template_frame, listvariable= self.anime_listbox_items)
        self.anime_listbox.grid(row=1, column=2, **self.padding, sticky="we")

        delete_anime_button = Button(self.anime_template_frame, text="Delete selected",
                                     command= self.delete_anime_template)
        delete_anime_button.grid(row=1, column=3, padx=(0, 10))

        anime_entry = Entry(self.anime_template_frame, textvariable=self.new_anime_template, width=50)
        anime_entry.grid(row=2, column=2, **self.padding)

        add_anime_button = Button(self.anime_template_frame, text="Add template",
                                  command= self.add_anime_template)
        add_anime_button.grid(row=2, column=3, padx=(0, 10))

    def center_window(self: tkinter.Toplevel):
        #TODO: center window in screen
        pass