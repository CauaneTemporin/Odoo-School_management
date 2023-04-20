# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'School Management',
    'version': '13.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'School Management Sofware',
    'description': """Module to Management School""",
    'depends': ['base', 'mail', 'website'],
    'data': [
        'security/ir.model.access.csv',
        #'static/src/xml/home_screen.xml',
        'static/src/xml/assets.xml',
        'static/src/xml/classes_screen.xml',
        'static/src/xml/teacher_screen.xml',
        'static/src/xml/matter_screen.xml',
        'static/src/xml/views.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/matter.xml',
        'views/classes.xml',
        'views/actions.xml',
        'views/menus.xml',
        'views/res_users.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
