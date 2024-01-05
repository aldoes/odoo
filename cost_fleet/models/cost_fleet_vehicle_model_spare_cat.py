# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetVehicleModelSpareCat(models.Model):
   _name = 'cost.fleet.vehicle.model.spare.cat'
   _description = 'Consumable Category'
   
   name = fields.Char(string="Spare")


