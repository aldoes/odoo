# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetModelBudgetService(models.Model):
   _name = 'cost.fleet.model.budget.services.line'
   _description = 'Link the model Vehicle Budget with rutine services'

   budget_id = fields.Many2one('cost.fleet.vehicle.model.budget',string='Budget', require=True)
   service_type_id = fields.Many2one('fleet.service.type',string='Services', require=True)
   currency_id = fields.Many2one('res.currency',string='Currency', require=True)
   value = fields.Monetary(string='Value', require=True)
   km_use = fields.Integer(string="life (km)")
   obs = fields.Text(string="Description")





