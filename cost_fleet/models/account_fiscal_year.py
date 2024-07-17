#  Copyright 2020 Simone Rubino - Agile Business Group
#  License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression


class AccountFiscalYear(models.Model):
    _inherit= "account.fiscal.year"
    _description = "Fiscal Year"

    name = fields.Char(
        required =True,
        translate = True
    )
    is_open = fields.Boolean(
        default = True,
        required = True,
        string = "Is open?"
    )
    