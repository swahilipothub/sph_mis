# -*- coding: utf-8 -*-
{
    'name': "Swahilipot",

    'summary': """
        Membership Information System
    """,

    'description': """
        Membership Information System for Swahilipot Hub
    """,

    'author': "Swahilipot Hub",
    'website': "http://www.swahilipothub.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Membership',
    'version': '12.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/membership_invoice_views.xml',
        # 'data/membership_data.xml',
        'views/product_views.xml',
        'views/partner_views.xml',
        'report/report_membership_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'sequence': 1,
}