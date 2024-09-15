# -*- coding: utf-8 -*-
from odoo import models, fields,api
from datetime import datetime

BUDGET_TYPES = [
    ('mant_rut', 'Mantenimiento Rutinario'),
    ('mant_prev', 'Mantenimiento Preventivo'),
    ('rep', 'Prevision de Reparaciones'),
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
        store=True,
        ondelete='restrict',
  )
  service_price = fields.Monetary(string='Costo',
    currency_field='currency_id'
  )
  supplier_taxes_id = fields.Many2many('account.tax',
        string='Impuesto Proveedor', 
        domain=[('type_tax_use', '=', 'purchase')],
        # default=lambda self: self.env.companies.account_purchase_tax_id or self.env.companies.root_id.sudo().account_purchase_tax_id,
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
        compute='_compute_amount', 
        readonly=True
  )
  currency_id = fields.Many2one(comodel_name='res.currency', default=lambda self: self.env.company.currency_id, string='Moneda', store=False)
  budget_date_upd= fields.Datetime(string="Ult. Actualizacion")

  @api.depends('service_price','km_use')
  def _compute_amount(self):
      for budget in self:
        budget.amount_total=0
        for det in budget.consum_cat_line_ids:
            budget.amount_total += (det.cost_unit*det.qty)
        budget.amount_total += budget.service_price
        budget.costKm_total = budget.amount_total/budget.km_use

  def update_budget_cost(self):
      self.ensure_one()
      for line in self:
          line.consum_cat_line_ids.calculate_price_unit()
          line._compute_amount()
          line.budget_date_upd=fields.Datetime.now()

  def get_budgets_by_models(self, models):
        budgets = self.env['cost.fleet.vehicle.model.budget']
        for model in models:
            domain=[('model_ids','in', model.id),]            
            if( list_budgets := self.search(domain)):
              budgets+=list_budgets
        return budgets
