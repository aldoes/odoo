# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetVehicleModelFuels(models.Model):
   _name = 'cost.fleet.vehicle.model.fuels'
   _description = 'Fuels enabled for model'
   
   vehicle_id = fields.Many2one(comodel_name='fleet.vehicle',string='Vehicle',ondelete="cascade")
   fuel_cat_id = fields.Many2one(
        comodel_name='product.category',
        string='Fuel Category',
        domain="[('complete_name','like','Fuel /')]",
        ondelete="restrict"
   )
   fuel_effic = fields.Float(string="Km/lt",required=True, default=10.0)


