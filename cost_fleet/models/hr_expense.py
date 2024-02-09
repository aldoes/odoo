from datetime import date
from odoo import api, fields, models, _

class HrExpense(models.Model):
    _inherit = "hr.expense"

    #can_mod_unit_price = fields.Boolean(string="Can Change Unit Price")

    def get_last_expense_line_to_date(self, product,date_limit = date.today()):
        product.ensure_one()
        last_expense_line = list_expense_lines = self.get_expenses_lines_to_date(product,date_limit)
        if len(list_expense_lines) > 1:
            last_expense_line = list_expense_lines.sorted(key=lambda r: r.move_id.invoice_date, reverse=True)[0]

        return last_expense_line 


    def get_expenses_lines_to_date(self, product, date_limit= date.today()):
        product.ensure_one()
        domain = [('product_id', '=', product.id), 
                ('state', '=', "done"),
                ('date', '<=', date_limit)] 

        return self.search(domain)