from contextlib import closing

from Data.globalData import TemplateType, database
from tkinter import messagebox
import sqlite3


def get_templates(template_type : TemplateType):
    """
    Read the templates from the DB
    :param template_type: type of the templates to obtain
    :return: a list of templates
    """
    with sqlite3.connect(database) as sqliteConnection:
        try:
            cursor = sqliteConnection.cursor()
            if template_type == TemplateType.anime:
                table = "AnimeTemplates"
            else:
                table = "MangaTemplates"

            query = f"SELECT Template from {table}"
            cursor.execute(query)
            result = cursor.fetchall()

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error occurred - {error}")

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
            #TODO: insert a new template in the DB
            if template_type == TemplateType.anime:
                table = "AnimeTemplates"
            else:
                table = "MangaTemplates"

            query = f"INSERT INTO {table}(Template, Is_Active, Is_Default) VALUES(?,?,?)"
            cursor.execute(query, (template, False, False))

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error occurred - {error}")

        finally:
            if cursor:
                cursor.close()

def delete_template(template, template_type: TemplateType):
    """
    Delete a template from the templates DB
    :param template_type: type of the passed template
    :param template: template to delete
    """
    with sqlite3.connect(database) as sqliteConnection:
        try:
            cursor = sqliteConnection.cursor()
            #TODO: delete a template from the DB

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error occurred - {error}")

        finally:
            if cursor:
                cursor.close()


def change_active_template(selected_template, template_type : TemplateType):
    """
    Sets a template as the active one
    :param template_type: type of the passed template
    :param selected_template: template to be set as active
    """
    with sqlite3.connect(database) as sqliteConnection:
        try:
            cursor = sqliteConnection.cursor()
            #TODO: change the active template

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error occurred - {error}")

        finally:
            if cursor:
                cursor.close()

