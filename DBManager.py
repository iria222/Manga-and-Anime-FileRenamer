from Data.globalData import TemplateType, database, default_anime_template,default_manga_template
import Data.globalData as globalData
from tkinter import messagebox
import sqlite3


def get_templates(template_type : TemplateType) -> list:
    """
    Read the templates from the DB
    :param template_type: type of the templates to obtain
    :return: a list of templates
    """
    result = []
    with sqlite3.connect(database) as sqliteConnection:
        try:
            cursor = sqliteConnection.cursor()
            if template_type == TemplateType.anime:
                table = "AnimeTemplates"
            else:
                table = "MangaTemplates"

            query = f"SELECT Template from {table}"
            cursor.execute(query)
            result = [item[0] for item in cursor.fetchall()]

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error occurred when accessing the database - {error}")
        finally:
            if cursor:
                cursor.close()
            return result


def insert_template(template, template_type : TemplateType):
    """
    Insert a new template in the templates DB
    :param template: template to insert
    :param template_type: type of the passed template
    """
    with sqlite3.connect(database) as sqliteConnection:
        try:
            cursor = sqliteConnection.cursor()
            if template_type == TemplateType.anime:
                table = "AnimeTemplates"
            else:
                table = "MangaTemplates"

            query = f"INSERT INTO {table}(Template, Is_Active, Is_Default) VALUES(?,?,?)"
            cursor.execute(query, (template, False, False))

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error occurred when accessing the database - {error}")
            return 1
        finally:
            if cursor:
                cursor.close()

def delete_template(template, template_type: TemplateType):
    """
    Delete a template from the templates DB
    :param template_type: type of the passed template
    :param template: template to delete
    """
    if is_default(template, template_type):
        messagebox.showerror("Error", "The default template cannot be deleted")
        return 1

    with sqlite3.connect(database) as sqliteConnection:
        try:
            cursor = sqliteConnection.cursor()

            if template_type == TemplateType.anime:
                table = "AnimeTemplates"
                default_template = default_anime_template
            else:
                table = "MangaTemplates"
                default_template = default_manga_template

            #The deleted template is the active one
            if template == get_active_template(template_type):
                change_active_template(default_template, template_type)

            query = f"DELETE FROM {table} WHERE Is_Default = FALSE AND Template = '{template}'"
            cursor.execute(query)

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error occurred when accessing the database - {error}")
            return 1

        finally:
            if cursor:
                cursor.close()

def is_default(template, template_type: TemplateType) -> bool:
    """
    Checks if a template is the default one
    :param template: template to check
    :param template_type: type of the passed template
    :return: True if the template is the default
             False if not
    """
    with sqlite3.connect(database) as sqliteConnection:
        try:
            cursor = sqliteConnection.cursor()
            if template_type == TemplateType.anime:
                table = "AnimeTemplates"
            else:
                table = "MangaTemplates"

            query = f"SELECT EXISTS(SELECT 1 FROM {table} WHERE Is_Default = TRUE AND Template = '{template}')"
            cursor.execute(query)
            result = cursor.fetchone()[0]

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error occurred when accessing the database - {error}")

        finally:
            if cursor:
                cursor.close()
            return result

def change_active_template(selected_template, template_type : TemplateType):
    """
    Sets a template as the active one
    :param template_type: type of the passed template
    :param selected_template: template to be set as active
    """
    with sqlite3.connect(database) as sqliteConnection:
        try:
            cursor = sqliteConnection.cursor()
            if template_type == TemplateType.anime:
                table = "AnimeTemplates"
            else:
                table = "MangaTemplates"

            query = f"UPDATE {table} SET Is_Active = ? WHERE Is_Active = TRUE"
            cursor.execute(query, [False])
            query = f"UPDATE {table} SET Is_Active = ? WHERE Template = '{selected_template}'"
            cursor.execute(query, [True])

            if template_type == TemplateType.anime:
                globalData.anime_template = selected_template
            else:
                globalData.manga_template = selected_template

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error occurred when accessing the database - {error}")

        finally:
            if cursor:
                cursor.close()

def get_active_template(template_type : TemplateType):
    """
    Get the active template from DB
    :param template_type: type of the template to get
    :return: active template
    """
    result = ""
    with sqlite3.connect(database) as sqliteConnection:
        try:
            cursor = sqliteConnection.cursor()

            if template_type == TemplateType.anime:
                table = "AnimeTemplates"
            else:
                table = "MangaTemplates"

            query = f"SELECT Template FROM {table} WHERE Is_Active = TRUE"
            cursor.execute(query)
            result = cursor.fetchone()[0]

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error occurred when accessing the database - {error}")

        finally:
            if cursor:
                cursor.close()
            return result