from odoo import http
from odoo.http import request
from odoo.addons.web.controllers import main as web

class StudentDetail(http.Controller):

    @http.route('/student', auth='public', website=True)
    def student(self):
        print(self.env)
        student_records = request.env['school.student'].search([])
        return request.render('school_management.student_data', {"records": student_records})

    @http.route('/matter', auth='public', website=True)
    def matter(self):
        matter_records = request.env['school.matter'].search([])
        student = request.env.user.student_id
        if request.env.user:
            class_student = request.env['school.classes'].search([('students_id', 'in', student.id)])
            matter_records = matter_records.search([('id', 'in', class_student.teacher_ids.ids)])
        return request.render('school_management.matter_data', {"records": matter_records})

    @http.route('/classes', auth='public', website=True)
    def classes(self):
        classes_records = request.env['school.classes'].search([])
        student = request.env.user.student_id
        if request.env.user:
            classes_records = classes_records.search([('students_id', 'in', student.id)])
        return request.render('school_management.classes_data', {"records": classes_records})

    @http.route('/teacher', auth='public', website=True)
    def teacher(self):
        teacher_records = request.env['school.teacher'].search([])
        student = request.env.user.student_id
        if request.env.user:
            class_student = request.env['school.classes'].search([('students_id', 'in', student.id)])
            teacher_records = teacher_records.search([('id', 'in', class_student.teacher_ids.ids)])
        return request.render('school_management.teacher_data', {"records": teacher_records})

class Home(web.Home):
    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        response = super(Home, self).web_login(redirect, **kw)
        if kw.get('login', False):
            student = request.env['school.student'].search([('identity', 'ilike', kw['login'])])
        return response