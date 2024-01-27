# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

class FleetVehicle(models.Model):
    _inherit  = 'fleet.vehicle'

    fuel_enab_cat_ids = fields.One2many(
        comodel_name='cost.fleet.vehicle.fuel.cats.line', 
        inverse_name="vehicle_id", 
        string="Fuel Category Enabled")
    values_ids = fields.One2many(
        comodel_name='cost.fleet.vehicle.values.line', 
        inverse_name="vehicle_id", 
        string="Values for year")

    

  