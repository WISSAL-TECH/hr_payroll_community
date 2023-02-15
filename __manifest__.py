# -*- coding: utf-8 -*-

{
    'name': 'Odoo15 Payroll',
    'category': 'Generic Modules/Human Resources',
    'version': '15.0.1.1.0',
    'author': 'Odoo SA,Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'summary': 'Manage your employee payroll records',
    'images': ['static/description/banner.png'],
    'description': "Odoo 15 Payroll, Payroll, Odoo 15,Odoo Payroll, Odoo Community Payroll",
    'depends': [
        'hr_contract',
        'hr_holidays',
       
    ],
    'data': [
        'security/hr_payroll_security.xml',
        'security/ir.model.access.csv',
        'wizard/hr_payroll_payslips_by_employees_views.xml',
        'views/hr_leave_type_view.xml',
        'views/hr_contract_views.xml',
        'views/hr_salary_rule_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_employee_views.xml',
        'data/hr_payroll_sequence.xml',
        'views/hr_payroll_report.xml',
        'data/hr_payroll_data.xml',
        'wizard/hr_payroll_contribution_register_report_views.xml',
        'views/res_config_settings_views.xml',
        'views/report_contributionregister_templates.xml',
        'views/report_payslip_templates.xml',
        'views/report_payslipdetails_templates.xml',
    ],
    'demo': ['data/hr_payroll_demo.xml'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,

}
