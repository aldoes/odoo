# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

class AccountMoveEx(models.Model):
    _inherit = "account.move"

    def _get_last_purchase(self, product, date_limit= date.today()):      
        product.ensure_one()
        '''Condiciones
        id: del producto
        invoice_date: Fecha Factura tiene que ser menor o igual al fecha limite
        state: Debe existir Factura no anulada
        move_type: tipo factura
        display_type: el registro tiene q ser product
        '''
        domain = [('product_id', '=', product.id), ('display_type', '=', 'product'), ('move_id.move_type', '=', 'in_invoice'),('move_id.state', '!=', 'cancel'),('move_id.invoice_date', '<=', date_limit)]  
        list_purchase = self.env['account.move.line'].search(domain)
        if len(list_purchase) > 0:
            last_purchase = list_purchase.sorted(key=lambda r: r.move_id.invoice_date, reverse=True)[0]
        else:
            last_purchase = list_purchase
        return last_purchase

    

