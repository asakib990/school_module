from odoo import api, fields, models, _


class Section(models.Model):
    _name = "school.section"
    _description = "Section"
    
    name = fields.Char("Section Name", required=True)
    code = fields.Char("Section Code", required=True)