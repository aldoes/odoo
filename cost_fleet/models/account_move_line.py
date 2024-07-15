from datetime import date
from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def get_last_purchase_line_to_date(self, product,date_limit = date.today()):
        product.ensure_one()
        last_purchase_line = list_purchase_lines = self.get_purchases_lines_to_date(product,date_limit)
        if len(list_purchase_lines) > 1:
            last_purchase_line = list_purchase_lines.sorted(key=lambda r: r.move_id.invoice_date, reverse=True)[0]

        return last_purchase_line 


    def get_purchases_lines_to_date(self, product, date_limit= date.today()):
        product.ensure_one()
        domain = [('product_id', '=', product.id), 
                ('display_type', '=', 'product'), 
                ('move_id.move_type', '=', 'in_invoice'),
                ('move_id.state', '!=', 'cancel'),
                ('move_id.invoice_date', '<=', date_limit)] 

        return self.env['account.move.line'].search(domain)