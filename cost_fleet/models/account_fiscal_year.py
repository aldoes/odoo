#  Copyright 2020 Simone Rubino - Agile Business Group
#  License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from datetime import date


class AccountFiscalYear(models.Model):
    _inherit= "account.fiscal.year"
    _description = "Fiscal Year"
    _order = "year desc"

    # def _get_year_range(self,year_ini=date.today().year-10,year_qty=25):
    #     year_list=[]
    #     for i in range(year_qty):
    #         year_list.append((year_ini+i,str(year_ini+i)))  
    #     return year_list 
    
    name = fields.Char(
        required =True,
        translate = True
    )

    year = fields.Integer(string="year", default=date.today().year, required=True)

    is_open = fields.Boolean(
        default = True,
        required = True,
        string = "Is open?"
    )

