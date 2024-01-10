# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetVehicleModelBudgetServicesline(models.Model):
   _name = 'cost.fleet.vehicle.model.budget.services.line'
   _description = 'Line Links the model Budget with services'

   budget_id = fields.Many2one('cost.fleet.vehicle.model.budget',string='Budget', required=True,ondelete="cascade")
   service_type_id = fields.Many2one('fleet.service.type',string='Services', required=True,ondelete="restrict")
   currency_id = fields.Many2one('res.currency',string='Currency', required=True)
   value = fields.Monetary(string='Value', required=True)
   km_use = fields.Integer(string="life (km)", default=100)
   obs = fields.Text(string="Description")

    #TODO - crear campos compute del costo x km de la linea de servicio
    #TODO Agregar constraint UNIQUE budget_id,service_type_id



