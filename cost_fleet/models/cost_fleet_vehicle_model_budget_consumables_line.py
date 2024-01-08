# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetModelBudgetConsumablesline(models.Model):
   _name = 'cost.fleet.model.budget.consumables.line'
   _description = 'Line Links the model Budget with consumables'

   budget_id = fields.Many2one('cost.fleet.vehicle.model.budget',string='Budget', required=True)
   spare_cat_id = fields.Many2one('cost.fleet.vehicle.model.spare.cat',string='Consumables', required=True)
   qty = fields.Float(default=1.0,string='Quantity')   
   currency_id = fields.Many2one('res.currency',string='Currency', required=True)
   value = fields.Monetary(string='Value', required=True)
   km_use = fields.Integer(string="life (km)")
   obs= fields.Text(string="Description")





