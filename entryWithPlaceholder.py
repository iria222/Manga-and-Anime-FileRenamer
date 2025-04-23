import tkinter

class EntryWithPlaceholder(tkinter.Entry):
    def __init__(self, master, placeholder :str, placeholder_color = "grey", normal_color = "black"):
        super().__init__(master)
        self.placeholder_color = placeholder_color
        self.normal_color = normal_color
        self.placeholder_active = True

        self.config(fg = self.placeholder_color)
        self.insert(0,placeholder)
        self.bind("<FocusIn>", lambda x: self.on_focus_in())
        self.bind("<FocusOut>", lambda x: self.on_focus_out(placeholder))


    def on_focus_in(self):
        if self.placeholder_active:
            self.config(fg = self.normal_color)
            self.delete(0, "end")
            self.placeholder_active = False

    def on_focus_out(self, placeholder:str):
        if self.get() == "":
            self.insert(0, placeholder)
            self.config(fg = self.placeholder_color)
            self.placeholder_active = True