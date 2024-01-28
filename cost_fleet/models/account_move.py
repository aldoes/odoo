
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'    
    _sql_constraints = [('invoice_ref_uniq', 'unique(partner_id,ref )', "Duplicate the fiscal invoice reference"), ]

