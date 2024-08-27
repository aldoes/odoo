# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.addons.fleet.models.fleet_vehicle_model import FUEL_TYPES

FUEL_TYPES.extend([
        ('alcohol', 'Alcohol'),
        ('biflex', 'Gasolina-Alcohol'),
    ])

class FleetVehicleModel(models.Model):
    _inherit  = 'fleet.vehicle.model'
    budget_ids = fields.Many2many('cost.fleet.vehicle.model.budget', 
        'cost_fleet_vehicle_model_budget_fleet_vehicle_model_rel',
        'fleet_vehicle_model_id',
        'cost_fleet_vehicle_model_budget_id', 
        string="Presupuestos")
    
    

