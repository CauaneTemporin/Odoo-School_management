from odoo import fields, models

class SchoolStudent(models.Model):
    _name = "school.student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Student Table"

    information = fields.Char(String="Name", required=True)
    name = fields.Char(String="Name")
    age = fields.Integer(String="Age")
    birth_date = fields.Date(string="Birth Date")
    identity = fields.Char(String="Identity")
    mother_name = fields.Char(String="Mother name")
    general_grade = fields.Char(String="General grade", compute="_average_of_averages")
    father_name = fields.Char(String="Father_name")
    note = fields.Text(String="Notes")
    image = fields.Binary(String="Image")
    gender = fields.Selection([
        ('male', 'Masculino'),
        ('female', 'Feminino'),
        ('other', 'Outro')
    ], string='Gender', default='male')
    hour_shift = fields.Selection([
        ('morning', 'Manhã'),
        ('afternoon', 'Tarde'),
        ('night', 'Noite')
    ], string='HourShift', default='morning')


    class_id = fields.Many2one('school.classes', string='Classe')
    teacher_ids = fields.Many2many(related="class_id.teacher_ids")
    grades_id = fields.One2many('school.grades', 'student_id', string='Estudante')

    def _average_of_averages(self):
        for record in self:
            general_grade = 0
            if record.grades_id:
                for grade in record.grades_id:
                    general_grade += grade.final_grade
                record.general_grade = general_grade / len(record.grades_id)
            else:
                record.general_grade = 0
