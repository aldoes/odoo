# -*- coding: utf-8 -*-
from odoo import models, fields

class CostFleetModelBudget(models.Model):
   _name = 'cost.fleet.vehicle.model.budget'
   _description = 'Link the model Vehicle with consumables'

   model_ids = fields.Many2many('fleet.vehicle.model',string='Models', required=True)
   name= fields.Char(string='Title', required=True)
   services_ids = fields.One2many(comodel_name='cost.fleet.vehicle.model.budget.services.line', inverse_name="budget_id", string="Services")
   consumable_cat_ids = fields.One2many(comodel_name='cost.fleet.vehicle.model.budget.consumables.line', inverse_name="budget_id",string="Consumables")
   #TODO Campo sumatoria de lineas de servicios y consumibles

