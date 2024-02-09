from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    tax_include = fields.Boolean(string="Tax Include",default=False )


    @api.depends('taxes_id', 'list_price')
    def _compute_tax_string(self):
        for record in self:
            if record.tax_include:
                record.tax_string = record._construct_tax_string(record.list_price)
            else:
                record.tax_string = record.list_price