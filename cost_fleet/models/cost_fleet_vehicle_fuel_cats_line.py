# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetVehicleFuelCatsline(models.Model):
   _name = 'cost.fleet.vehicle.fuel.cats.line'
   _description = 'Fuels enabled for model'
   _sql_constraints = [('vehicle_catFuel_uniq', 'unique(vehicle_id ,fuel_cat_id)', "Duplicate Category in the same vehicle"),]
   
   vehicle_id = fields.Many2one(comodel_name='fleet.vehicle',string='Vehicle',ondelete="cascade")
   fuel_cat_id = fields.Many2one(
        comodel_name='product.category',
        string='Fuel Category',
        domain="[('complete_name','like','Fuel /')]",
        ondelete="restrict"
   )
   fuel_effic = fields.Float(string="Km/lt",required=True, default=10.0)
   default_for_cost = fields.Boolean(string="default for cost")



