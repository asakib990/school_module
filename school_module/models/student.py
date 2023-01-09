from odoo import api, models, fields, _

class Student(models.Model):
    _name = "school.student"
    _description = "student"

    name = fields.Char("Student Name", required=True)
    email = fields.Char("Student Email")
    phone = fields.Char("Student Phone Number")
    birth_date = fields.Date("Student Birth Date")
    gender = fields.Selection([("Male","Male"),("Female","Female")], "Gender")