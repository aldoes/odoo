
from datetime import date
from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'    
    _sql_constraints = [('invoice_ref_uniq', 'unique(partner_id,ref )', "Duplicate the fiscal invoice reference"), ]
    

    def get_last_purchased_line_to_date(self, product, date_limit= date.today()):      
            product.ensure_one()
            '''Get last purchase line of active purchase invoiced before or on limit date or return false  '''
            return self.env['account.move.line'].get_last_purchase_line_to_date(product, date_limit)


