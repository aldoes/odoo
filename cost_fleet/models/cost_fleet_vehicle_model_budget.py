# -*- coding: utf-8 -*-
from odoo import models, fields,api
from datetime import datetime

BUDGET_TYPES = [
    ('mant_rut', 'Mantenimiento Rutinario'),
    ('mant_prev', 'Mantenimiento Preventivo'),
    ('rep', 'Reparaciones'),
    ('imp', 'Impuesto Vehicular'),
    ('otro', 'Otras Previsiones'),
]
class CostFleetVehicleModelBudget(models.Model):
  _name = 'cost.fleet.vehicle.model.budget'
  _description = 'Link the model Vehicle with consumables'
  _sql_constraints = [('km_use_greaterThanZero',  'CHECK(km_use>0)', "Km use must be greater than zero"), ]

  name= fields.Char(string='Servicio', required=True)
  model_ids = fields.Many2many('fleet.vehicle.model',string='Models', required=True)  
  budg_type = fields.Selection(BUDGET_TYPES, 'Tipo', default='mant_rut', required=True)
  partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
      #   compute='_compute_partner_id', inverse='_inverse_partner_id',  readonly=False, precompute=True,
        store=True,
        ondelete='restrict',
    )
  service_price = fields.Monetary(string='Costo',
  currency_field='currency_id'
    # digits='Product Price', 
    # groups="base.group_user"
  )
  currency_id = fields.Many2one(comodel_name='res.currency', default=lambda self: self.env.company.currency_id, string='Moneda')
  supplier_taxes_id = fields.Many2many('account.tax',
        string='Impuesto Proveedor', 
        domain=[('type_tax_use', '=', 'purchase')],
        default=lambda self: self.env.companies.account_purchase_tax_id or self.env.companies.root_id.sudo().account_purchase_tax_id,
  )
  km_use = fields.Integer(string="km Estimados", default=5000)
  obs= fields.Text(string="Details")
  consum_cat_line_ids = fields.One2many(comodel_name='cost.fleet.vehicle.model.budget.consumables.line', 
      inverse_name="budget_id",
      string="Items",
      copy=True
  )
  amount_total = fields.Monetary(
        string='Total',
        compute='_compute_amount', 
        readonly=True
  )
  costKm_total = fields.Monetary(
        string='Total Cost Km',
        readonly=True
  )
  currency_id = fields.Many2one(comodel_name='res.currency', default=lambda self: self.env.company.currency_id, string='Moneda')
  budget_date_upd= fields.Datetime(string="Ult. Actualizacion")

  @api.depends('service_price')
  def _compute_amount(self):
      for budget in self:
        budget.amount_total=0
        for det in budget.consum_cat_line_ids:
            budget.amount_total += (det.cost_unit*det.qty)
        budget.amount_total += budget.service_price
        budget._compute_costKm()
  
  @api.depends('km_use')
  def _compute_costKm(self):
      for budget in self:
          budget.costKm_total=budget.amount_total/budget.km_use

  def update_budget_cost(self):
      self.ensure_one()
      for line in self:
          line.consum_cat_line_ids.calculate_price_unit()
          line._compute_amount()
          line.budget_date_upd=fields.Datetime.now()
          # line.budget_date_upd=fields.Datetime.to_string(datetime.now())
      #TODO Campo sumatoria de lineas de servicios y consumibles

  def get_budgets_by_models(self, models):
        budgets = self.env['cost.fleet.vehicle.model.budget']
        for model in models:
            domain=[('model_ids','in', model.id),]            
            if( list_budgets := self.search(domain)):
              budgets+=list_budgets
        return budgets





    #             budgets_list = self.get_spare_for_model(model, category,True)
    #             if (spare_list):
    #                 if(len(spare_list)>1):
    #                     higherCost_spare += spare_list[0]   
    #                 else:
    #                     higherCost_spare+= spare_list
    #     if ( len(higherCost_spare)>1):
    #         higherCost_spare= higherCost_spare.sorted(key=lambda r: r.last_cost, reverse=True)[0]
    #     return higherCost_spare
    # pass