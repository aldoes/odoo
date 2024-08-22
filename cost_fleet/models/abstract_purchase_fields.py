from datetime import date
from odoo import api, fields, models, _

class AbstractPurchaseFields(models.AbstractModel):
    _name ='abstract.purchase.fields'   
    _description = 'Abstract Model with last purchase data fields and its methods to models derivated from product.product model' 
    #all cost must by in company.currency_id
    last_cost = fields.Monetary(string='Last Cost',
                                      currency_field='info_currency_id',
                                      compute='_compute_last_adquire_cost',store=False)
    info_currency_id = fields.Many2one(comodel_name='res.currency', default=lambda self: self.env.company.currency_id, string='Cost Currency', store=False)
    last_info_date = fields.Date(string="Cost Date", store=False)
        
    def _compute_last_adquire_cost(self, date_limit= date.today()):
        #TODO - calculate cost whitout taxes
        # if not exists purchase record then get the Supplierinfo cost,if not, then is Zero
        for record in self:        
            record.info_currency_id = self.env.company.currency_id 
            record.last_info_date = date_limit 
            if (purchaseLine := self.env['account.move'].get_last_purchased_line_to_date(record.product_id, date_limit)):
                record.last_cost = purchaseLine.currency_id._convert(purchaseLine.price_unit,record.info_currency_id)     
                record.last_info_date = purchaseLine.move_id.invoice_date 
            elif (supplierCost := self.env["product.supplierinfo"].get_highest_cost_supplierinfo_line(record.product_id)):
                record.last_cost = supplierCost.currency_id._convert(supplierCost.price,record.info_currency_id)                 
            else:
                record.last_cost = record.standard_price or 0.0

            
            

    def action_purchase_history(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("purchase.action_purchase_history")
        action['domain'] = [('state', 'in', ['purchase', 'done']), ('product_id', '=', self.product_id.id)]
        action['display_name'] = _("Purchase History for %s", self.product_id.display_name)  
        return action
