from odoo import api, fields, models, _


class Course(models.Model):
    _name = "school.course"
    _description = "Course"
    
    name = fields.Char("Course Name", required=True)
    code = fields.Char("Course Code", required=True)