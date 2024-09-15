from datetime import date
from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def get_last_purchase_line_to_date(self, product,date_limit = date.today(),highest=False):
        product.ensure_one()
        last_purchase_line = self.get_purchases_lines_to_date(product,date_limit)
        if (len(last_purchase_line) > 1):
            if(highest):
                last_purchase_line = last_purchase_line.sorted(key=lambda r: r.price_unit, reverse=True)[0]
            else:
                last_purchase_line = last_purchase_line[0]
        return last_purchase_line 


    def get_purchases_lines_to_date(self, product, date_limit= date.today()):
        product.ensure_one()
        purchases_lines = self.env['account.move.line']
        domain = [('product_id', '=', product.id), 
                ('display_type', '=', 'product'), 
                ('move_id.move_type', '=', 'in_invoice'),
                ('move_id.state', '!=', 'cancel'),
                ('move_id.invoice_date', '<=', date_limit)] 
        if (result:=self.search(domain)):
            purchases_lines = result
            if(len(purchases_lines)>1):
                purchases_lines = purchases_lines.sorted(key=lambda r: r.move_id.invoice_date, reverse=True)
        return purchases_lines