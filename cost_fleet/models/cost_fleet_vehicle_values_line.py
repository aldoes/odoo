# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import date

class CostFleetVehicleValuesline(models.Model):
   _name = 'cost.fleet.vehicle.values.line'
   _description = 'Values of the vehicle'
   _sql_constraints = [('value_fiscalyear_uniq', 'unique(vehicle_id ,fiscal_year_id)', "Duplicate value in the same fiscal year"), ]

   vehicle_id = fields.Many2one(comodel_name='fleet.vehicle',string='Vehicle',ondelete="cascade")
   fiscal_year_id = fields.Many2one(comodel_name='account.fiscal.year',string='Fiscal year',ondelete="cascade")
   currency_id = fields.Many2one('res.currency',string='Currency', required=True)
   value = fields.Monetary(string='Value', required=True)
   km_use = fields.Integer(string="life (km)", default=100000)

   def get_last_value_to_year(self, vehicles, year=date.today().year):
      # for vehicle in vehicles:
      #       last_value_line = list_values_lines = self.get_list_value_lines_to_year(vehicle,year)
      # # vehicle.ensure_one()
      # 
      # if len(last_value_line)==0:
        
       
      # else:
      #    if len(last_value_line) > 1:
      #       last_value_line = list_values_lines.sorted(key=lambda r: r.fiscal_year_id, reverse=True)[0]

      # return last_value_line 

      pass
      

   def get_list_value_lines_to_year(self, vehicle, year=date.today().year):
        vehicle.ensure_one()
        domain = [('vehicle_id', '=', vehicle.id), 
                ('fiscal_year_id.year', '<=', year)] 
        return self.search(domain)

   #TODO Agregar constraint para bloquear cambio o eliminacion de registro por periodo contable abierto



