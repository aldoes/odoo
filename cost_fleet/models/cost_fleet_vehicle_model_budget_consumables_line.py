# -*- coding: utf-8 -*-

from odoo import models, fields,api

class CostFleetVehicleModelBudgetConsumablesline(models.Model):
   _name = 'cost.fleet.vehicle.model.budget.consumables.line'
   _description = 'Line Links the model Budget with consumables'
   _sql_constraints = [('spare_cat_uniq', 'unique(budget_id,spare_cat_id )', "Duplicate consumable or spare part line"), ]

   budget_id = fields.Many2one('cost.fleet.vehicle.model.budget',string='Budget', required=True, ondelete="cascade")
   spare_cat_id = fields.Many2one('cost.fleet.vehicle.model.spare.cat',string='Consumables', required=True,ondelete="restrict")
   qty = fields.Float(default=1.0,string='Quantity')   
   km_use = fields.Integer(string="life (km)", default=100)
   last_cost = fields.Monetary(string="Last Cost", store=False, readonly=True)
   date_last_purchase = fields.Date(string="Date of Last Purchase", store=False,readonly=True)
   cost_km = fields.Monetary(string='Cost/Km',compute='_compute_cost_km')
   obs= fields.Text(string="Details")
   
   @api.depends('spare_cat_id','qty','km_use')
   def _compute_cost_km(self):      
      for line in self:
         ####
            '''
               TODO last_cost: usar calculo de costo sin impuestos
               TODO : Debe traer el ultimo costo sin impueso de la pieza comprada de la categoria de ese consumible/repuesto
               que haya sido adquirido pare ese modelo.
               TODO : Adaptar productos para registrar compras de repuestos e insumos para el modelo de vehiculo               
            '''
         ####
      pass

   






