# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetVehicleModelBudgetServicesline(models.Model):
   _name = 'cost.fleet.vehicle.model.budget.services.line'
   _description = 'Line Links the model Budget with services'

   budget_id = fields.Many2one('cost.fleet.vehicle.model.budget',string='Budget', required=True,ondelete="cascade")
   service_type_id = fields.Many2one('fleet.service.type',string='Services', required=True)
   currency_id = fields.Many2one('res.currency',string='Currency', required=True)
   value = fields.Monetary(string='Value', required=True)
   km_use = fields.Integer(string="life (km)")
   obs = fields.Text(string="Description")





