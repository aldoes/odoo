# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import date

class CostFleetVehicleValuesline(models.Model):
   _name = 'cost.fleet.vehicle.values.line'
   _description = 'Values of the vehicle'
   _sql_constraints = [('value_fiscalyear_uniq', 'unique(vehicle_id ,fiscal_year_id)', "Duplicate value in the same fiscal year"), 
                       ('kmUse_greaterThanZero', 'km_use>0', "km use must be greater than zero")]

   vehicle_id = fields.Many2one(comodel_name='fleet.vehicle',string='Vehicle',ondelete="cascade")
   fiscal_year_id = fields.Many2one(comodel_name='account.fiscal.year',string='Fiscal year',ondelete="cascade")
   currency_id = fields.Many2one(comodel_name='res.currency',string='Currency', related='vehicle_id.currency_id',store=False)
   value = fields.Monetary(string='Value', required=True)
   km_use = fields.Integer(string="life (km)", default=300000)

   def get_last_value_to_year(self, vehicle, year=date.today().year):    
      vehicle.ensure_one() 
      last_value_line = self.get_list_value_lines_to_year(vehicle,year)
      if (len(last_value_line)>1):
         last_value_line = last_value_line.sorted(key=lambda r: r.fiscal_year_id.year, reverse=True)[0]
      return last_value_line 

   def get_list_value_lines_to_year(self, vehicle, year=date.today().year):
      vehicle.ensure_one()
      domain = [('vehicle_id', '=', vehicle.id), 
         ('fiscal_year_id.year', '<=', year)] 
      value_list = self.env['cost.fleet.vehicle.values.line'].new({
         'vehicle_id': vehicle.id,
         'value': vehicle.net_car_value or 1,
         'currency_id': vehicle.currency_id or self.env.company.currency_id,
         'km_use':  vehicle.km_use or 1
         })
      if(result:=self.search(domain)):
         value_list = result
      return value_list

   #TODO Agregar constraint para bloquear cambio o eliminacion de registro por periodo contable abierto



