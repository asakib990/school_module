from odoo import api, fields, models, _


class Section(models.Model):
    _name = "school.registration"
    _description = "Registrations"
    
    section_id = fields.Many2one("school.section", "Section")
    course_id = fields.Many2one("school.course", "Course ID")
    teacher_id = fields.Many2one("school.teacher", "Teacher",)
    student_ids = fields.Many2many("school.student", "registration_student_rel", "registraion_id", "student_id", "Student List")