# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetVehicleModelSpareCat(models.Model):
   _name = 'cost.fleet.vehicle.model.spare.cat'
   _description = 'Consumable Category'
   _order="sequence desc"
   
   name = fields.Char(string="Spare")
   sequence = fields.Integer(string="Order")


