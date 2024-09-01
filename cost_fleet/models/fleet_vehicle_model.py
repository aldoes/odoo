# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.addons.fleet.models.fleet_vehicle_model import FUEL_TYPES

FUEL_TYPES.extend([
        ('alcohol', 'Alcohol'),
        ('biflex', 'Gasolina-Alcohol'),
    ])

class FleetVehicleModel(models.Model):
    _inherit  = 'fleet.vehicle.model'
    budget_ids = fields.Many2many('cost.fleet.vehicle.model.budget', 
        'cost_fleet_vehicle_model_budget_fleet_vehicle_model_rel',
        'fleet_vehicle_model_id',
        'cost_fleet_vehicle_model_budget_id', 
        string="Presupuestos")
    consum_km_cost = fields.Monetary(
        string='Costo Consumibles Km',
        compute='_compute_consum_km_cost', 
        readonly=True
    )
    currency_id = fields.Many2one(comodel_name='res.currency', default=lambda self: self.env.company.currency_id, string='Moneda')
    def _compute_consum_km_cost(self):
        for model in self:
            model.consum_km_cost=0
            for budget in model.budget_ids:
                model.consum_km_cost+=budget.costKm_total
    