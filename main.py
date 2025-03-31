import tkinter
from tkinter.ttk import Notebook

from GUI.animeFrame import AnimeFrame
from GUI.configurationFrame import ConfigurationFrame
from GUI.mangaFrame import MangaFrame

current_directory : tkinter.StringVar



class Application:

    def __init__(self):
        main_window = tkinter.Tk()
        center_window(main_window)
        main_window.title("File renamer")

        main_window.resizable(False, False)
        notebook = Notebook(main_window)

        manga_frame = MangaFrame()
        anime_frame = AnimeFrame()
        config_frame = ConfigurationFrame()

        notebook.add(manga_frame, text = "Manga", padding= (20, 20, 20, 20))
        notebook.add(anime_frame, text = "Anime", padding= (20, 20, 20, 20))
        notebook.add(config_frame, text = "Configuration", padding= (20, 20, 20, 20))

        notebook.pack(expand = True, fill = "both")

        main_window.mainloop()


def center_window(window):
    window.eval('tk::PlaceWindow . center')


def main():
    Application()
    return 0

if __name__ == '__main__':
    main()