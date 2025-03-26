from globalData import TemplateType


def get_templates(template_type : TemplateType):
    """
    Read the templates from the DB
    :param template_type: type of the templates to obtain
    :return: a list of templates
    """
    #TODO: read templates from DB
    pass

def insert_template(template, template_type : TemplateType):
    """
    Insert a new template in the templates DB
    :param template: template to insert
    :param template_type: type of the passed template
    """
    #TODO: insert a new template in the DB
    pass

def delete_template(template, template_type: TemplateType):
    """
    Delete a template from the templates DB
    :param template_type: type of the passed template
    :param template: template to delete
    """
    #TODO: delete a template from the DB
    pass

def change_active_template(selected_template, template_type : TemplateType):
    """
    Sets a template as the active one
    :param template_type: type of the passed template
    :param selected_template: template to be set as active
    """
    #TODO: change the active template