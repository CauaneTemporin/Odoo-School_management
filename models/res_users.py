from odoo import fields, models, api
import datetime

class Users(models.Model):
    _inherit = "res.users"
    _description = "Users Table"

    student_id = fields.Many2one('school.student', string="Aluno relacionado")

    @api.onchange('student_id')
    def _change_student_id(self):
        self.name = self.student_id.name
        self.login = self.student_id.identity


    @api.model
    def create(self, vals):
        result = super(Users, self).create(vals)
        if vals.get('student_id', False):
            cpf_format = vals.get('login').replace('.', '').replace('-', '')
            password = f'{cpf_format[0:5]}@{datetime.datetime.now().strftime("%Y")}'
            result.password = password
            result.write({"groups_id": [(6, self.id, [61, 8, 30])]})

        return result