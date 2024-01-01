# -*- coding: utf-8 -*-
{
    'name': "Cost",

    'summary': "Cost Module",

    'description': """
Module for Cost
    """,

    'author': "Aldo Escobar",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Cost',
    'version': '0.1',

    # any module necessary for this one to work correctly
    #'depends': ['base','purchase','fleet','hr'],.
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        #'security/cost_security.xml',
        #'security/ir.model.access.csv',
        'data/cost_fleet_fuel_data.xml',
        #'data/cost.fleet.vehicle.model.consumable.cat.csv'
        'views/cost_fleet_fuel_view.xml', 
        #'views/cost_fleet_vehicle_model_consumable_cat.xml'   
        #'views/cost_fleet_vehicle_ext_view_form.xml'    
    ],
}

