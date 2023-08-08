# -*- coding: utf-8 -*-
{
    'name': 'Hashcode Helpdesk',
    'license': 'LGPL-3',
    'summary': """This module allow you manage your customer support ticket, ticket portal, billings for support, Timesheets.""",
    'description': """
                    Website Helpdesk Support Ticket
                    """,
    'author': "Hash Code IT solutions",
    'website': "http://www.hashcodeit.com",
    'support': 'support@hashcodeit.com',
    "version": "16.0.1.0.0",
    'category': 'Services/Project',
    'depends': ['sale_management', 'hr_timesheet', 'project', 'portal', 'sales_team', 'crm', 'account', 'website',
                'sale_timesheet'
                # 'website_portal',
                ],
    'data': [
        'wizard/task_timesheet_invoice.xml',  # 16-1-2019
        'report/support_request.xml',
        'datas/helpdesk_support_sequence.xml',
        'datas/mail_template_ticket.xml',
        'datas/helpdesk_team_data.xml',
        'datas/helpdesk_stages_data.xml',
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'views/website_template.xml',
        'views/website_mail_message_template.xml',
        'views/helpdesk_stages_views.xml',
        'views/helpdesk_support_view.xml',
        'views/ticket_type_view.xml',
        'views/type_of_subject_view.xml',
        'views/helpdesk_support_template.xml',
        'views/hr_timesheet_sheet_view.xml',
        'views/support_team_view.xml',
        'views/my_ticket.xml',
        #  odoo12      'views/ticket_attachment.xml',
        'views/successfull.xml',
        'views/task.xml',
        'views/feedback.xml',
        'views/thankyou.xml',
        #  odoo12      'report/helpdesk_analysis.xml',
        'views/analytic_account_view.xml',
        'views/res_partner_form_view.xml',
        'views/project_form_view.xml',
        'views/project_task_form_view.xml',
        'views/helpdesk_invoice_view.xml',  # 16-1-2019
        #         'report/weekly_time_sheet_report_view.xml',
        #         'wizard/weekly_timesheet_report.xml',
        # 'views/report_analysis.xml',
    ],
    'images': [
        'static/description/img.png',
    ],
    'installable': True,
    'application': False,
    # 'auto_install' : True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
