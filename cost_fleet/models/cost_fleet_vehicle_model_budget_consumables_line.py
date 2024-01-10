# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetVehicleModelBudgetConsumablesline(models.Model):
   _name = 'cost.fleet.vehicle.model.budget.consumables.line'
   _description = 'Line Links the model Budget with consumables'

   budget_id = fields.Many2one('cost.fleet.vehicle.model.budget',string='Budget', required=True, ondelete="cascade")
   spare_cat_id = fields.Many2one('cost.fleet.vehicle.model.spare.cat',string='Consumables', required=True,ondelete="restrict")
   qty = fields.Float(default=1.0,string='Quantity')   
   currency_id = fields.Many2one('res.currency',string='Currency', required=True)
   value = fields.Monetary(string='Value', required=True)
   km_use = fields.Integer(string="life (km)", default=100)
   obs= fields.Text(string="Description")

   #TODO - crear campos compute del costo x km de la linea de consumible
   #TODO Agregar constraint UNIQUE budget_id,spare_cat_id





