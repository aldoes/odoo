# -*- coding: utf-8 -*-
{
    'name': "Fleet Cost",

    'summary': "Fleet Cost Module",

    'description': """
Module for Cost of Fleet
    """,

    'author': "Aldo Escobar",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Cost',
    'version': '0.2.0',

    # any module necessary for this one to work correctly
    #'depends': ['base','purchase','fleet','hr'],.
    'depends': ['base','purchase','fleet'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/cost.fleet.vehicle.model.spare.cat.csv",
        #"data/fleet_model_service.xml", TODO: falta cargar datos
        "data/cost_fleet_vehicle_data.xml",
        "data/cost_fleet_fuel_data.xml",
        "views/cost_fleet_views.xml",
        "views/cost_fleet_vehicle_model_budget_views.xml",
        "views/fleet_views.xml",
    ],
}

