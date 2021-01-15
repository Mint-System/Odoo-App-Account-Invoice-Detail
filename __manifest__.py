# -*- coding: utf-8 -*-
{
    'name': "Account Invoice Detail",

    'summary': """
        Add field salesperson to invoice.
    """,

    'description': """
        Add field salesperson to invoice.
    """,

    'author': "Mint System GmbH",
    'website': "https://www.mint-system.ch",
    'category': 'Accounting',
    'version': '14.0.1.0.0',

    'depends': ['account'],

    'data': [
        'views/account_report_invoice_document.xml',
    ],

    'installable': True,
    'application': False,
}