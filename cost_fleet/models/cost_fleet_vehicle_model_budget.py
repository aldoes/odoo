# -*- coding: utf-8 -*-
from odoo import models, fields

class CostFleetModelBudget(models.Model):
   _name = 'cost.fleet.vehicle.model.budget'
   _description = 'Link the model Vehicle with consumables'

   model_id = fields.Many2one('fleet.vehicle.model',string='Model', required=True)
   name= fields.Char()
   services_ids = fields.One2many(comodel_name='cost.fleet.model.budget.services.line', inverse_name="budget_id", string="Services")
   consumable_cat_ids = fields.One2many(comodel_name='cost.fleet.model.budget.consumables.line', inverse_name="budget_id",string="Consumables")


