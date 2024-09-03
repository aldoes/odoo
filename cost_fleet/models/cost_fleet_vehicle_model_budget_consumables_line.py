# -*- coding: utf-8 -*-

from odoo import models, fields,api

class CostFleetVehicleModelBudgetConsumablesline(models.Model):
   _name = 'cost.fleet.vehicle.model.budget.consumables.line'
   # _inherit = ['abstract.kmcost.fields'] 
   _description = 'Line Links the model Budget with consumables'
   _sql_constraints = [('spare_cat_uniq', 'unique(budget_id,spare_cat_id )', "Duplicate consumable or spare part line"), ]

   budget_id = fields.Many2one(
      comodel_name='cost.fleet.vehicle.model.budget',
      string='Budget', 
      readonly=True,
      index=True,
      auto_join=True,
      required=True, 
      ondelete="cascade"
   )
   spare_cat_id = fields.Many2one('product.category',
      string='Consumables', 
      required=True,
      ondelete="restrict"
   )   
   qty = fields.Float(default=1.0,string='Quantity')   
   cost_unit = fields.Monetary(
        string='Unit Cost',
        readonly=True,
        store=True,
      #   digits='Product Price'
   )   
   cost_date = fields.Date(
      string='Date Cost',
      store=True,
      readonly=True,
   )
   cost_km = fields.Monetary(
        string='Cost Km',
        readonly=True,
        store=False,
      #   digits='Product Price',
        compute ="_calculate_km_cost"
   )

   obs = fields.Text(string="Details")
   currency_id = fields.Many2one(comodel_name='res.currency', default=lambda self: self.env.company.currency_id, string='Moneda', store=False)

   @api.depends('cost_unit')
   def _calculate_km_cost(self):
      for line in self:
            line.cost_km=(line.cost_unit*line.qty)/line.budget_id.km_use

   def calculate_price_unit(self):
        for line in self:
            spare = self.env['cost.fleet.vehicle.model.spare'].get_higherCost_spare_inCategory_for_model(line.budget_id.model_ids, line.spare_cat_id)
            line.cost_unit = spare.last_cost or 0.0
            line.cost_date= spare.last_info_date
            # if not line.product_id or line.display_type in ('line_section', 'line_note'):
            #     continue
            # if line.move_id.is_sale_document(include_receipts=True):
            #     document_type = 'sale'
            # elif line.move_id.is_purchase_document(include_receipts=True):
            #     document_type = 'purchase'
            # else:
            #     document_type = 'other'
            # line.price_unit = line.product_id._get_tax_included_unit_price(
            #     line.move_id.company_id,
            #     line.move_id.currency_id,
            #     line.move_id.date,
            #     document_type,
            #     fiscal_position=line.move_id.fiscal_position_id,
            #     product_uom=line.product_uom_id,)

   # @api.depends('spare_cat_id','qty','km_use')
   # def _compute_cost_km(self):      
   #    for line in self:
   #       line.cost_km = 0.0
   #       ####
   #       '''
   #          TODO last_cost: usar calculo de costo sin impuestos
   #          que haya sido adquirido pare ese modelo.
   #          TODO : Adaptar productos para registrar compras de repuestos e insumos para el modelo de vehiculo               
   #       '''
   #       ####
   #    pass

   






