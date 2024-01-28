# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.addons.fleet.models.fleet_vehicle_model import FUEL_TYPES

class costFleetVehicleFuel(models.Model):
    _name="cost.fleet.vehicle.fuel" 
    _inherits = {'product.product': 'product_id'}
    _description = 'Vehicle Fuel'
    
    product_id = fields.Many2one(
        'product.product', 'Product Id',
        auto_join=True, index=True, ondelete="cascade", required=True)
    
    def action_purchase_history(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("purchase.action_purchase_history")
        action['domain'] = [('state', 'in', ['purchase', 'done']), ('product_id', '=', self.product_id.id)]
        action['display_name'] = _("Purchase History for %s", self.product_id.display_name)
  
        return action
