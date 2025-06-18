from enum import Enum

database = "./Data/RenamerTemplates.db"

class TemplateType(Enum):
    manga = 1
    anime = 2

default_anime_template = """{name} S{season_number:02d}E{episode_number:02d}"""
default_manga_template = """{name} V{volume_number:02d}"""

manga_extensions = ["cbz", "cbr", "epub", "mobi", "pdf"]
video_extensions = ["MP4", "MOV", "AVI","FLV", "MKV","WMV","AVCHD","WEBM","MPEG-4"]

anime_template = default_anime_template
manga_template = default_manga_template

