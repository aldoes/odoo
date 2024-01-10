# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetVehicleValuesline(models.Model):
   _name = 'cost.fleet.vehicle.values.line'
   _description = 'Values of the vehicle'
   
   vehicle_id = fields.Many2one(comodel_name='fleet.vehicle',string='Vehicle',ondelete="cascade")
   currency_id = fields.Many2one('res.currency',string='Currency', required=True)
   value = fields.Monetary(string='Value', required=True)
   km_use = fields.Integer(string="life (km)", default=100000)

   #TODO Agregar constraint para bloquear cambio o eliminacion de registro por periodo contable abierto
   #TODO Agregar constraint UNIQUE periodo (year),vehicle_id


