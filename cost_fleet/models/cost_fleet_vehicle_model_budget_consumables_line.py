# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetModelBudgetConsumable(models.Model):
   _name = 'cost.fleet.model.budget.consumables.line'
   _description = 'Link the model Vehicle Budget with consumables'

   budget_id = fields.Many2one('cost.fleet.vehicle.model.budget',string='Budget', require=True)
   cons_cat_id = fields.Many2one('cost.fleet.vehicle.model.consumable.cat',string='Consumables', require=True)
   qty = fields.Float(default=1.0,string='Quantity')   
   currency_id = fields.Many2one('res.currency',string='Currency', require=True)
   value = fields.Monetary(string='Value', require=True)
   km_use = fields.Integer(string="life (km)")
   obs=fields.Text(string="Description")





