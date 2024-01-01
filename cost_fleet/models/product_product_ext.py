# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

class ProductProductExt(models.Model):
    _inherit = 'product.product'

    last_cost = fields.Monetary(string="Last Cost", compute='_compute_last_cost')
    date_last_purchase = fields.Date(string="Date of Last Purchase", store=False)

    def _compute_last_cost(self,date_limit= date.today()):
        for product in self:
                purchase = self.env['account.move']._get_last_purchase(product, date_limit)
                if purchase:
                        product.last_cost = purchase.price_unit
                        product.date_last_purchase= purchase.move_id.invoice_date
                else:
                    product.last_cost = 0.0
                    product.date_last_purchase = date.today()


    

