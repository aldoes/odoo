# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date
from odoo.addons.fleet.models.fleet_vehicle_model import FUEL_TYPES

FUEL_TYPES.extend([
        ('alcohol', 'Alcohol'),
        ('biflex', 'Gasolina-Alcohol'),
    ])

class FleetVehicleModelEx(models.Model):
    _inherit  = 'fleet.vehicle.model'
    _description = 'Vehicle Model Extender'
    
    

