
from datetime import date
from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'    
    _sql_constraints = [('invoice_ref_uniq', 'unique(partner_id,ref )', "Duplicate the fiscal invoice reference"), ]
    
    def get_last_purchase_line(self, product, date_limit= date.today()):      
        product.ensure_one()
        '''Get last purchase line of active purchase invoiced before or on limit date or return false  '''
        last_purchase = False
        domain = [('product_id', '=', product.id), 
                  ('display_type', '=', 'product'), 
                  ('move_id.move_type', '=', 'in_invoice'),
                  ('move_id.state', '!=', 'cancel'),
                  ('move_id.invoice_date', '<=', date_limit)]  
        list_purchase = self.env['account.move.line'].search(domain)
        if len(list_purchase) > 0:
            last_purchase = list_purchase.sorted(key=lambda r: r.move_id.invoice_date, reverse=True)[0]
        return last_purchase

