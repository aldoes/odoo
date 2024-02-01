# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models
from odoo.addons.fleet.models.fleet_vehicle_model import FUEL_TYPES

class costFleetVehicleFuel(models.Model):
    _name="cost.fleet.vehicle.fuel" 
    _inherit = ['abstract.purchase.fields']
    _inherits = {'product.product': 'product_id'}
    _description = 'Vehicle Fuel'
    
    product_id = fields.Many2one(
        'product.product', 'Product Id',
        auto_join=True, index=True, ondelete="cascade", required=True)
    
    