from odoo import fields, models

class SchoolMatter(models.Model):
    _name = "school.matter"
    inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Matter Table"

    information = fields.Char(String="Name", required=True)
    name = fields.Char(String="Name")
    time = fields.Char(String="Time")