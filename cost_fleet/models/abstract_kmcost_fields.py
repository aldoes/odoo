from odoo import api, fields, models, _

class AbstractKmCostFields(models.AbstractModel):
    _name ='abstract.kmcost.fields'   
    _description = 'Abstract Model with Km cost fields and its methods' 

    qty = fields.Float(default=1.0,string='Quantity')   
    costkm_km_est = fields.Integer(string="Estimate Use (km)", default=1)
    costkm = fields.Monetary(string='Cost/Km',compute='_compute_km_cost', currency_field='costkm_currency_id', store=True)
    costkm_currency_id =  fields.Many2one('res.currency',string='Last Purchase Currency')
    
    def recalculate_km_cost(self):
        self._compute_km_cost()
     
    def _compute_km_cost(self):
            for record in self:
                pass 
                # record.cost_km = record.last_purch_cost / record.qty / record.km_use

     #TODO - El km_cost debe estar en moneda local, los costos pueden estan en moneda extranjera
