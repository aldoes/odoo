from datetime import date
from odoo import api, fields, models, _

class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    def get_last_expense_line_to_date(self, product, date_limit= date.today()):      
                product.ensure_one()
                '''Get last expense line of active and done expense before or on limit date or return empty record  '''
                return self.env['hr.expense'].get_last_expense_line_to_date(product,date_limit)

