# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetVehicleModelBudgetConsumablesline(models.Model):
   _name = 'cost.fleet.vehicle.model.budget.consumables.line'
   _description = 'Line Links the model Budget with consumables'
   _sql_constraints = [('spare_cat_uniq', 'unique(budget_id,spare_cat_id )', "Duplicate consumable or spare part line"), ]

   budget_id = fields.Many2one('cost.fleet.vehicle.model.budget',string='Budget', required=True, ondelete="cascade")
   spare_cat_id = fields.Many2one('cost.fleet.vehicle.model.spare.cat',string='Consumables', required=True,ondelete="restrict")
   qty = fields.Float(default=1.0,string='Quantity')   
   currency_id = fields.Many2one('res.currency',string='Currency', required=True)
   value = fields.Monetary(string='Value', required=True,default=1.0)
   km_use = fields.Integer(string="life (km)", default=100)
   cost_km = fields.Monetary(string='Cost/Km',compute='_compute_cost_by_km', stored=True)
   obs= fields.Text(string="Description")
   
   @api.depends('value','km_use')
   def _compute_cost_by_km(self):
      for line in self
         if line.km_use = 0.0:
            line.cost_km = 0.0
         else:
            line.cost_km = line.value / line.km_use






