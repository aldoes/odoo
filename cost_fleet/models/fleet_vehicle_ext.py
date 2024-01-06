# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

class FleetVehicleEx(models.Model):
    _inherit  = 'fleet.vehicle'
    _description = 'Vehicle Extender'

    #fuel_effic = fields.Float(string="Km/lt",required=True, default=10.0)

    # def _compute_defaul_fuel_effic(self):        
    #     for vehicle in self:
    #         domain = [('brand_id.id','=',vehicle.brand_id.id)]
    #         model_keff = self.env['fleet.vehicle.model'].search(domain, limit=1)
    #         if  model_keff:
    #              self.fuel_effic = model_keff
    #         else:
    #             self.fuel_effic = 10.0