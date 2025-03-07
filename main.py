import tkinter
from tkinter.ttk import Notebook

from animeFrame import AnimeFrame
from mangaFrame import MangaFrame

current_directory : tkinter.StringVar



class Application():

    def __init__(self):
        main_window = tkinter.Tk()
        main_window.title("File renamer")

        notebook = Notebook(main_window)

        manga_frame = MangaFrame()
        anime_frame = AnimeFrame()

        notebook.add(manga_frame, text = "Manga")
        notebook.add(anime_frame, text = "Anime")
        notebook.pack(expand = True, fill = "both")
        main_window.mainloop()



def main():
    my_app = Application()
    return(0)

if __name__ == '__main__':
    main()