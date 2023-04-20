from odoo import fields, models

class SchoolGrades(models.Model):
    _name = "school.grades"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Grades Table"

    information = fields.Char(String="Name")
    matter_id = fields.Many2one('school.matter', 'Matérias', readonly=False)
    proof1 = fields.Integer(String="Prova")
    activities = fields.Integer(String="Trabalhos")
    presence = fields.Integer(String="Presença")
    final_grade = fields.Integer(String="Média Final", compute="_calc_final_grade")
    student_id = fields.Many2one('school.student', string='Notas')

    def _calc_final_grade(self):
        for record in self:
            proof = record.proof1
            activities = record.activities
            presence = record.presence
            record.final_grade = (proof + activities + presence) / 3
