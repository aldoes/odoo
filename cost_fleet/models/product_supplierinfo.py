# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SupplierInfo(models.Model):
    _inherit = "product.supplierinfo"
    _sql_constraints =  [('partnerPrice_delay_unique', 'unique(partner_id,product_id ,delay)', "You can't insert another Partner price in the same delay term"), ]

    update_date = fields.Datetime(string="Ult. Actualización", store=True,default=fields.Datetime.now())

    def get_cost_supplierinfo_line(self, product,highest=True):
        product.ensure_one()
        supplierinfo_line_highest_cost = list_supplierinfo_lines = self.get_supplierinfo_lines(product)
        if len(list_supplierinfo_lines) > 1:
            supplierinfo_line_highest_cost = list_supplierinfo_lines.sorted(key=lambda r: r.price, reverse=highest)[0]

        return supplierinfo_line_highest_cost 

    def get_supplierinfo_lines(self, product):
        product.ensure_one()
        domain = [('product_tmpl_id', '=', product.product_tmpl_id.id),] 

        return self.env['product.supplierinfo'].search(domain)

    @api.onchange('price')
    def _onchange_price(self):
        self.update_date= fields.Datetime.now()
