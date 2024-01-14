# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models

class ProductProduct(models.Model):
    _inherit = 'product.template'
    
    #TODO hacer visible la moneda de costo
    #TODO agregar el tipo Repuesto
    #detailed_type = fields.Selection(selection_add=[('spare', 'Spare')])
#     detailed_type = fields.Selection([
#         ('consu', 'Consumable'),
#         ('service', 'Service'),
#         ('spare', 'Spare')], string='Product Type', default='consu', required=True,
#         help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
#              'A consumable product is a product for which stock is not managed.\n'
#              'A service is a non-material product you provide.')
    
    model_ids = fields.Many2many('fleet.vehicle.model',string='Models', required=True) 



    

