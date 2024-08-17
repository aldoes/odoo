from odoo import api, fields, models, _

class AbstractKmCostFields(models.AbstractModel):
    _name ='abstract.kmcost.fields'   
    _description = 'Abstract Model with Km cost fields and its methods' 
    _sql_constraints = [('km_est_gtOne', 'CHECK (costkm_km_est > 0.0)', "km estimate must be grant than zero"),]

    qty = fields.Float(default=1.0,string='Quantity')   
    km_use = fields.Integer(string="Estimate Use (km)", default=5000)

    # costkm = fields.Monetary(string='Cost/Km',compute='_compute_km_cost', currency_field='info_currency_id', store=True)
    # info_currency_id = fields.Many2one(comodel_name='res.currency', default=lambda self: self.env.company.currency_id, string='Cost Currency', store=False)
    
    # def recalculate_km_cost(self):
    #     self._compute_km_cost()
     
    # def _compute_km_cost(self):
    #         for record in self:
    #          record.cost_km = record.last_purch_cost / record.qty / record.km_use

     #TODO - El km_cost debe estar en moneda local, los costos pueden estan en moneda extranjera
