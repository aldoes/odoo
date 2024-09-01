# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models
from odoo.addons.fleet.models.fleet_vehicle_model import FUEL_TYPES

class costFleetVehicleFuel(models.Model):
    _name="cost.fleet.vehicle.fuel" 
    _inherit = ['abstract.purchase.fields']
    _inherits = {'product.product': 'product_id'}
    _description = 'Vehicle Fuel'
    
    product_id = fields.Many2one(
        'product.product', 'Product Id',
        auto_join=True, index=True, ondelete="cascade", required=True)

    def get_fuels_by_cat(self, category, sortBy_highest_cost=False):
        category.ensure_one()
        domain=[('categ_id.complete_name','like','Fuel / '+ category.name)]
        list_fuels = self.env['cost.fleet.vehicle.fuel'].new({
            'name': "INDETERMINADO",
        })        
        if(results:=self.search(domain)):
                list_fuels=results
        if (sortBy_highest_cost and len(list_fuels)>1):
            list_fuels = list_fuels.sorted(key=lambda r: r.last_cost, reverse=True)
        return list_fuels
    
    def get_default_categ(self):
        category = self.env['product.category'].search([('id','=', self.env.ref('cost_fleet.cat_fuel').id),])
        return category


    
    