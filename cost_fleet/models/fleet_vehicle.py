# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

class FleetVehicle(models.Model):
    _inherit  = 'fleet.vehicle'

    fuel_enab_cat_ids = fields.One2many(
        comodel_name='cost.fleet.vehicle.fuel.cats.line', 
        inverse_name="vehicle_id", 
        string="Fuel Category Enabled")
    
    values_ids = fields.One2many(
        comodel_name='cost.fleet.vehicle.values.line', 
        inverse_name="vehicle_id", 
        string="Values for year")
    km_use = fields.Integer(string="life (km)", default=300000)
    years_use = fields.Integer(string="life (years)", default=5)
    odometer_unit = fields.Selection([
        ('kilometers', 'km'),
        ('miles', 'mi')
        ], 'Odometer Unit', default='kilometers', required=True, readonly=True)
    currency_id = fields.Many2one(comodel_name='res.currency',string='Moneda Compra', related='company_id.currency_id',store=True,  required=True)
    cost_value_km = fields.Monetary(string='Last Km Value Cost',
                                      currency_field='cost_curr_id',
                                      compute='_compute_last_cost_value_km',
                                      readonly=True)
    cost_fuel_km = fields.Monetary(string='Last Km Fuel Cost',
                                      currency_field='cost_curr_id',
                                      compute='_compute_last_cost_fuel_km',
                                      readonly=True)
    cost_consu_km = fields.Monetary(string='Last Km Consumable Cost',
                                      currency_field='cost_curr_id',
                                      compute='_compute_last_cost_cons_km',
                                      readonly=True)
    cost_total_km = fields.Monetary(string='Last Km Consumable Cost',
                                      currency_field='cost_curr_id',
                                      compute='_compute_last_cost_total_km',
                                      readonly=True)
    cost_curr_id = fields.Many2one(comodel_name='res.currency', related='company_id.currency_id',string='Local Currency', readonly=True, store=False)
        
    budget_ids = fields.Many2many(comodel_name='cost.fleet.vehicle.model.budget', 
        compute='get_model_budget_ids',
        string="Presupuestos")

    def get_model_budget_ids(self):
        for line in self:
            line.budget_ids= self.env['cost.fleet.vehicle.model.budget'].get_budgets_by_models(line.model_id)

    def get_line_fuel_cat_cost_def(self):
        vehicle = self
        vehicle.ensure_one()
        domain = [('vehicle_id', '=', vehicle.id)]
        return vehicle.fuel_enab_cat_ids.search(domain,order='priority')[0] 
        
    #TODO convertir a moneda local los costos
    def _compute_last_cost_value_km(self):        
        for vehicle in self:
            vehicle.cost_value_km = vehicle.get_cost_vehicle_by_km()

    def _compute_last_cost_fuel_km(self):        
        for vehicle in self:
            vehicle.cost_fuel_km = vehicle.get_cost_fuel_by_km()

    def _compute_last_cost_cons_km(self):        
        for vehicle in self:
            vehicle.cost_consu_km=vehicle.model_id.consum_km_cost

    def _compute_last_cost_total_km(self):        
        for vehicle in self:
           vehicle.cost_total_km = vehicle.cost_value_km + vehicle.cost_fuel_km + vehicle.cost_consu_km


    def get_cost_vehicle_by_km(self, date_limit= date.today()):
        vehicle = self
        vehicle.ensure_one()
        value_line = self.env['cost.fleet.vehicle.values.line'].get_last_value_to_year(vehicle)
        return round(value_line.currency_id._convert(value_line.value,self.env.company.currency_id)/value_line.km_use,0)


    def get_cost_fuel_by_km(self, date_limit= date.today()):
        vehicle = self
        vehicle.ensure_one()
        fuel_line = vehicle.get_line_fuel_cat_cost_def()
        #TODO traer la ultima compra de combustible registrada para ese vehiculo
        #use function get_last_fuel_purchase_for_vehicule()
        #sino
        #TODO Valor default 1.0
        #Trae el mayor costo del combustible de la categoria prioritaria del vehiculo
        return self.env['cost.fleet.vehicle.fuel'].get_fuels_by_cat(fuel_line.fuel_cat_id, True)[0].last_cost/fuel_line.fuel_effic
        
    
    #Buscar la ultima compra del combustible de este vehiculo
    def get_last_fuel_purchase_for_vehicule(self):
        # vehicle = self
        # vehicle.ensure_one()
        return False