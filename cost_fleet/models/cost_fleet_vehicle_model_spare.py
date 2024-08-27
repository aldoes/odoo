# -*- coding: utf-8 -*-

from odoo import models, fields

class CostFleetVehicleModelSpare(models.Model):
   _name = 'cost.fleet.vehicle.model.spare'
   _inherit = ['abstract.purchase.fields']
   _inherits = {'product.product': 'product_id'}
   _description = 'Vehicle Spare and Consumable'
   _order="sequence desc"
   
   model_ids = fields.Many2many('fleet.vehicle.model',string='Models', required=True)
   product_id = fields.Many2one(
      'product.product', 'Product Id',
       auto_join=True, index=True, ondelete="cascade", required=True)
   km_use = fields.Integer(string="Estimate Use (km)", default=5000)

   def get_spare_for_model(self, model, categories=None, sortBy_highest_cost=False):
        model.ensure_one()        
        domain=[('model_ids','in', model.id),]
        if(categories):
            domain.append(('categ_id','in', categories.ids))
        list_spare=self.search(domain)
        if (sortBy_highest_cost and len(list_spare)>1):
            list_spare = list_spare.sorted(key=lambda r: r.last_cost, reverse=True)
        return list_spare

   def get_higherCost_spare_inCategory_for_model(self, models, category):
        category.ensure_one()
        spare_list = self.env['cost.fleet.vehicle.model.spare']
        for model in models:
                items = self.get_spare_for_model(model, category,True)
                if (items):
                    spare_list += items[0]        
        if ( len(spare_list)>1):
            spare_list = spare_list.sorted(key=lambda r: r.last_cost, reverse=True)
        return spare_list[0]

