# -*- coding: utf-8 -*-
{
    'name': "currency",

    'summary': "Currency tools",

    'description': """
    Module for currency Tools 
    """,

    'author': "Aldo Escobar",
    'website': "",
    'category': 'Account',
    'version': '17.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

   

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/currency_menu.xml",
        # "views/account_fiscal_year_views.xml",
    ],
    'license':"LGPL-3",
}

