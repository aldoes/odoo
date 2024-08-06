# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

class FleetVehicle(models.Model):
    _inherit  = 'fleet.vehicle'

    # fuel_enab_cat_ids = fields.One2many(
    #     comodel_name='cost.fleet.vehicle.fuel.cats.line', 
    #     inverse_name="vehicle_id", 
    #     string="Fuel Category Enabled")
    
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
    cost_curr_id = fields.Many2one(comodel_name='res.currency', related='company_id.currency_id',string='Local Currency', readonly=True, store=False)

    #TODO convertir a moneda local los costos
    def _compute_last_cost_value_km(self):        
        for vehicle in self:
            vehicle.cost_value_km=0.0
        #####call vehicle.get_cost_vehicle_by_km(vehicle)
        #     vehicle.cost_value_curr_id=self.env.company.currency_id 
        #     computed_cost = self.get_cost_vehicle_by_km(vehicle,date.today())            
        #     vehicle.cost_value_km=computed_cost.value/computed_cost.km_use
        #     vehicle.cost_value_curr=computed_cost.currency_id

    def _compute_last_cost_fuel_km(self):        
        for vehicle in self:
            vehicle.cost_fuel_km=0.0
        #####call vehicle.get_cost_fuel_by_km(vehicle)

    def _compute_last_cost_cons_km(self):        
        for vehicle in self:
            vehicle.cost_consu_km=0.0
        #####call vehicle.get_cost_consumables_by_km(vehicle)

    def get_cost_vehicle_by_km(self, vehicle, date_limit= date.today()):
        vehicle.ensure_one()
        pass

    def get_cost_fuel_by_km(self, vehicle,date_limit= date.today()):
        vehicle.ensure_one()
        pass

    def get_cost_consumables_by_km(self, vehicle,date_limit= date.today()):
        vehicle.ensure_one()
        pass

# net_car_value = fields.Float(string="Purchase Value")

    # odometer = fields.Float(compute='_get_odometer', inverse='_set_odometer', string='Last Odometer',
    #     help='Odometer measure of the vehicle at the moment of this log')

    #   def _get_odometer(self):
    #     FleetVehicalOdometer = self.env['fleet.vehicle.odometer']
    #     for record in self:
    #         vehicle_odometer = FleetVehicalOdometer.search([('vehicle_id', '=', record.id)], limit=1, order='value desc')
    #         if vehicle_odometer:
    #             record.odometer = vehicle_odometer.value
    #         else:
    #             record.odometer = 0

    #  def _set_odometer(self):
    #     for record in self:
    #         if record.odometer:
    #             date = fields.Date.context_today(record)
    #             data = {'value': record.odometer, 'date': date, 'vehicle_id': record.id}
    #             self.env['fleet.vehicle.odometer'].create(data)


    

  