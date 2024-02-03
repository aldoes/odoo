# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SupplierInfo(models.Model):
    _inherit = "product.supplierinfo"
    _sql_constraints =  [('partnerPrice_delay_unique', 'unique(partner_id ,delay)', "You can't insert another Partner price in the same delay term"), ]


    def get_highest_cost_supplierinfo_line(self, product):
        product.ensure_one()
        supplierinfo_line_highest_cost = list_supplierinfo_lines = self.get_supplierinfo_lines(product)
        if len(list_supplierinfo_lines) > 1:
            supplierinfo_line_highest_cost = list_supplierinfo_lines.sorted(key=lambda r: r.price, reverse=True)[0]

        return supplierinfo_line_highest_cost 
        #TODO - Calcular precio sin impuesto


    def get_supplierinfo_lines(self, product):
        product.ensure_one()
        domain = [('product_tmpl_id', '=', product.product_tmpl_id.id),] 

        return self.env['product.supplierinfo'].search(domain)