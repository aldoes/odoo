from datetime import date
from odoo import api, fields, models, _

class AbstractPurchaseFields(models.AbstractModel):
    _name ='abstract.purchase.fields'   
    _description = 'Abstract Model with last purchase data fields and its methods' 
    last_purch_cost = fields.Monetary(string='Last Cost',
                                      currency_field='last_purch_currency_id',
                                      compute='_compute_last_cost', 
                                      store=True)
    last_purch_currency_id = fields.Many2one('res.currency',string='Last Purchase Currency')
    last_purch_date = fields.Date(string="Date Last Purchase")
    
    def recalculate_last_cost(self):
        self._compute_last_cost()

        
    def _compute_last_cost(self, date_limit= date.today()):
        for record in self:
            purchase = self.env['account.move'].get_last_purchase_line(record.product_id, date_limit)
            if purchase:
                record.last_purch_cost = purchase.price_unit
                record.last_purch_currency_id = self.env.company.currency_id
                record.last_purch_date = purchase.move_id.invoice_date
            else:
                record.last_purch_cost = 1.0
                record.last_purch_currency_id = self.env.company.currency_id
                record.last_purch_date = date_limit
    
    
    def action_purchase_history(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("purchase.action_purchase_history")
        action['domain'] = [('state', 'in', ['purchase', 'done']), ('product_id', '=', self.product_id.id)]
        action['display_name'] = _("Purchase History for %s", self.product_id.display_name)  
        return action
