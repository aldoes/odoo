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
   unit_price = fields.Monetary(string='Unit Price', required=True,default=1.0, help="Price with tax")
   taxes_id = fields.Many2one('account.tax', string='Taxes', domain=['|', ('active', '=', False), ('active', '=', True)], context={'active_test': False})
   km_use = fields.Integer(string="life (km)", default=100)
   cost_km = fields.Monetary(string='Cost/Km',compute='_compute_cost_by_km', stored=True)
   obs= fields.Text(string="Details")
   
   @api.depends('qty','unit_price','km_use')
   def _compute_cost_by_km(self):
      for line in self
         if line.km_use = 0.0:
            line.cost_km = 0.0
         else:
            line.cost_km = line.unit_price / (line.axes_id.amount/100) * qty / line.km_use #formula provisoria

   #TODO usar calculo de impuesto incluido o no






