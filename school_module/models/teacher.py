from odoo import api, models, fields, _

class Student(models.Model):
    _name = "school.teacher"
    _description = "Teacher"

    name = fields.Char("Teacher Name", required=True)
    email = fields.Char("Teacher Email")
    phone = fields.Char("Teacher Phone Number")
    birth_date = fields.Date("Teacher Birth Date")
    gender = fields.Selection([("Male","Male"),("Female","Female")], "Gender")