# -*- coding: utf-8 -*-
from odoo import models, fields

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

  name= fields.Char(string='Title', required=True)
  model_ids = fields.Many2many('fleet.vehicle.model',string='Models', required=True)  
  budg_type = fields.Selection(BUDGET_TYPES, 'Budget Type', default='mant_rut', required=True)
  partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
      #   compute='_compute_partner_id', inverse='_inverse_partner_id',  readonly=False, precompute=True,
        store=True,
        ondelete='restrict',
    )
  standard_price = fields.Monetary(string='Costo',
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
      string="Consumables Items",
      copy=True
  )

  # amount_total = fields.Monetary(
  #       string='Total',
  #       compute='_compute_amount', store=True, readonly=True
  # )
   # services_ids = fields.One2many(comodel_name='cost.fleet.vehicle.model.budget.services.line', inverse_name="budget_id", string="Services")


  # def _compute_amount(self):
  #   for line in self.consum_cat_line_ids:
  #     self.amount_total += 0.0
  #   pass

     #TODO Campo sumatoria de lineas de servicios y consumibles