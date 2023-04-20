from odoo import fields, models

class SchoolClasses(models.Model):
    _name = "school.classes"
    inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Classes Table"

    information = fields.Char(String="Name", required=True)
    name = fields.Char(String="Name")
    teacher_ids = fields.Many2many('school.teacher', 'school_teacher_rel', column1='class_id', column2='teacher_id', string='Professores')
    students_id = fields.One2many('school.student', 'class_id', string='Alunos')
