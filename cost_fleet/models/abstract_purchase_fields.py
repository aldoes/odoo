from datetime import date
from odoo import api, fields, models, _

class AbstractPurchaseFields(models.AbstractModel):
    _name ='abstract.purchase.fields'   
    _description = 'Abstract Model with last purchase data fields and its methods' 
    
    last_purch_cost = fields.Monetary(string='Last Cost',
                                      currency_field='last_purch_currency_id',
                                      compute='_compute_last_adquire_cost')
    last_purch_currency_id = fields.Many2one('res.currency',string='Last Purchase Currency', store=False)
    last_purch_date = fields.Date(string="Date Last Purchase", store=False)

        
    def _compute_last_adquire_cost(self, date_limit= date.today()):
        for record in self:
            purchaseLine = self.env['account.move'].get_last_purchased_line_to_date(record.product_id, date_limit)
            supplierCost = self.env["product.supplierinfo"].get_highest_cost_supplierinfo_line(record.product_id)

            record.last_purch_cost = (purchaseLine.price_unit if purchaseLine.move_id.invoice_date else (supplierCost.price if supplierCost.currency_id.id else 0.0))
            record.last_purch_currency_id = (purchaseLine.currency_id if purchaseLine.currency_id.id else (supplierCost.currency_id if supplierCost.currency_id.id else self.env.company.currency_id))
            record.last_purch_date = (purchaseLine.move_id.invoice_date if purchaseLine.move_id.invoice_date else date_limit)

            #TODO - mostrar el costo sin Impuesto
            #TODO - Si no existe compra, Traer el costo Anotado en Seccion Supplierinfo sino cero

    def action_purchase_history(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("purchase.action_purchase_history")
        action['domain'] = [('state', 'in', ['purchase', 'done']), ('product_id', '=', self.product_id.id)]
        action['display_name'] = _("Purchase History for %s", self.product_id.display_name)  
        return action
