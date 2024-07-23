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
    #currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    # value_currency_id = fields.Many2one('res.currency', string='Purchase Currency', required=True)
    # life_km = fields.Integer(string="life (km)", default=300000)

    def get_cost_vehicle_by_km(self, vehicle, date_limit= date.today()):
        vehicle.ensure_one() 
        pass
    
    def get_cost_value_by_km_for_year(self, vehicle,current_year=date.today().year):
        pass
  

    def get_cost_fuel_by_km(self, vehicle,date_limit= date.today()):
        pass

    def get_cost_consumables_by_km(self, vehicle,date_limit= date.today()):
        pass

        #TODO cambiar a visible <field name="currency_id" invisible="1"/> y poner al costado de compra
        #TODO cambiar ultimo odometro a Vida Estimada
    

  