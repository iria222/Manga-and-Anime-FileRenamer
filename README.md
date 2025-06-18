# Manga & Anime FileRenamer
## Description
Rename the files inside a folder using your preferred format. Only files with the supported extensions will be renamed. Others will be omitted.<br/>
This program is meant to be used to quickly rename manga, anime or TB shows' files.

## Supported file extensions
- Manga: cbr, cbz, epub, mobi, pdf.
- Anime/TV shows: mp4, mov, avi, flv, mkv, wmv, avchd, webm, mpeg-4.

## How to use
All supported files inside the selected folder will be renamed. If you don't want to modify some of the files' names, save them in a different folder before using the application.
### Renaming manga
<p align = center>
  <img src = https://github.com/user-attachments/assets/a07f00fa-37cc-4433-9482-e84b24107908 style ="width:50%; height:50%;">
</p>

Fields:
- Name: name of the manga.
- Starter number: starting value for numbering the files. If left empty, the default value (1) will be used.
- Folder directory: path to the folder that contains the files to be renamed. Subfolders will be ignored.

### Renaming anime/tv shows
<p align = center>
  <img src = https://github.com/user-attachments/assets/73ab1a39-2586-44ac-9fce-c27414a7f6c5 style ="width:50%; height:50%;">
</p>

Fields:
- Name: name of the anime or tv show.
- Starter number: starting value for numbering the files. If left empty, the default value (1) will be used.
- Season number: season number of the anime or TV show. If left empty, the default value (1) will be used.
- Folder directory: path to the folder that contains the files to be renamed. Subfolders will be ignored.

### Creating a new renaming template
<p align = center>
  <img src = https://github.com/user-attachments/assets/6c80cc25-4a47-4cc0-b8c1-8dda1cfb7809 style ="width:75%; height:75%;">
</p>
Both manga and anime templates can contain plain text, as well as the following placeholders (those marked with <code style="color : red">*</code> are compulsory).

For manga:
- <code style="color : red">*</code> {name} : it will be replaced by the contents of the `Name` field.
- <code style="color : red">*</code> {volume_number} : it will be replaced by a number. The files will be numbered in order starting by digit written in the `Starter number` field.

For anime:
- <code style="color : red">*</code> {name} : it will be replaced by the contents of the `Name` field.
- <code style="color : red">*</code> {episode_number} : it will be replaced by a number. The files will be numbered in order starting by digit written in the `Starter number` field.
- {season_number} : it will be replaced by the contents of the `Season number` field.

If you want the numeric values (volume_number, episode_number and season_number) to have a specific number of digits, you can do it by adding <code style="color : green">:0 number_of_digits d</code> at the end of the placeholder.

#### Example of correct renaming templates
`{name} V{volume_number:02d}` -> One Piece V01<br/>
`Manga {name} Volume {volume_number:02d}` -> Manga One Piece Volume 01<br/>
`{name} #{volume_number}` -> One Piece #1<br/>
<br/>
`{name} S{season_number:02d}E{episode_number:02d}` -> One Piece S01E01<br/>
`{name} E{episode_number:02d` -> One Piece E01<br/>
`{name} #{episode_number:03d}` -> One Piece #001<br/>




  
  

  
