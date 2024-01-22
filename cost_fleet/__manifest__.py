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
    'version': '0.2.0',

    # any module necessary for this one to work correctly
    #'depends': ['base','purchase','fleet','hr'],.
    'depends': ['base','purchase','fleet','account_fiscal_year'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",    
        #"data/fleet_model_service.xml", TODO: falta cargar datos
        "data/cost_fleet_vehicle_data.xml",
        "data/cost_fleet_fuel_data.xml",
        "data/cost_fleet_spare_cat_data.xml",
        "data/product.category.csv",
        "views/account_fiscal_year_views.xml",
        "views/product_category_views.xml",
        "views/cost_fleet_model_spare_views.xml",
        "views/cost_fleet_vehicle_fuel.xml",
        "views/fleet_views.xml",
        "views/cost_fleet_views.xml",
        "views/cost_fleet_menu.xml",
    ],
    'license':"LGPL-3",
}

