from odoo import fields, models

class SchoolTeacher(models.Model):
    _name = "school.teacher"
    inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Teacher Table"

    information = fields.Char(String="Name", required=True)
    name = fields.Char(String="Name")
    age = fields.Integer(String="Age")
    birth_date = fields.Date(string="Birth Date")
    identity = fields.Char(String="Identity")
    matter = fields.Char(String="Matter")
    mother_name = fields.Char(String="Mother name")
    father_name = fields.Char(String="Father_name")
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

    matter_id = fields.Many2one('school.matter', 'Matérias', readonly=False)


