# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    last_cost = fields.Monetary(string="Last Cost", compute='_compute_last_cost')
    date_last_purchase = fields.Date(string="Date of Last Purchase", store=False)
    
    
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
    
    #model_ids = fields.Many2many('fleet.vehicle.model',string='Models', required=True) 

    def _compute_last_cost(self,date_limit= date.today()):
        for product in self:
                product.last_cost = 0.0
                product.date_last_purchase = date_limit
                purchase = self.env['account.move']._get_last_purchase(product, date_limit)
                if purchase:
                        product.last_cost = purchase.price_unit
                        product.date_last_purchase= purchase.move_id.invoice_date
    
    def get_price_without_tax(self):
            pass


    

