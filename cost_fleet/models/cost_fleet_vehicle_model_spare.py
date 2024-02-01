# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetVehicleModelSpare(models.Model):
   _name = 'cost.fleet.vehicle.model.spare'
   _inherit = 'abstract.purchase.fields'
   _inherits = {'product.product': 'product_id'}
   _description = 'Vehicle Spare and Consumable'
   _order="sequence desc"
   
   model_ids = fields.Many2many('fleet.vehicle.model',string='Models', required=True)
   product_id = fields.Many2one(
      'product.product', 'Product Id',
       auto_join=True, index=True, ondelete="cascade", required=True)

   
   #TODO - tipo de producto repuesto, product category = spare


