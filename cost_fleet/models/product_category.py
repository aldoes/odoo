# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductCategoryEx(models.Model):
   _inherit = 'product.category'   
   _order="sequence desc"
   
   name = fields.Char('Name', index='trigram', required=True,translate=True)
   complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True,translate=True)  
   sequence = fields.Integer(string="Order")


