# -*- coding: utf-8 -*-
{
    'name': "Fleet Cost",

    'summary': "Fleet Cost Module",

    'description': """
Module for Cost of Fleet
    """,

    'author': "Aldo Escobar",
    'website': "",
    'category': 'Cost',
    'version': '17.0.0.3.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account_fiscal_year','purchase','fleet'],
    #'depends': ['base','purchase','fleet',"hr_expense",'account_fiscal_year'],
   

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        #"data/cost_fleet_vehicle_data.xml",
        "data/cost_fleet_fuel_data.xml",
        # "data/cost_fleet_spare_cat_data.xml",
        # "data/product.category.csv",
        # "views/account_fiscal_year_views.xml",
        "views/product_category_views.xml",
        # "views/cost_fleet_vehicle_model_spare_view.xml",
        "views/cost_fleet_vehicle_fuel_view.xml",
        # "views/fleet_views.xml",
        # "views/cost_fleet_vehicle_model_budget_view.xml",
       "views/cost_fleet_menu.xml",
    ],
    'license':"LGPL-3",
}

