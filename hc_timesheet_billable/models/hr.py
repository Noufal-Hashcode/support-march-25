from odoo import api, fields, models, _


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    ratio_factor = fields.Float(string='Ratio Factor', default=0.0)


class Timesheet(models.Model):
    _inherit = "account.analytic.line"

    ratio_factor = fields.Float(string='Ratio Factor', related='employee_id.ratio_factor')
    billable = fields.Float(string='Billable', compute='_compute_hc_billable')

    @api.depends('ratio_factor', 'unit_amount')
    def _compute_hc_billable(self):
        for rec in self:
            if rec.ratio_factor and rec.unit_amount:
                rec.billable = rec.ratio_factor * rec.unit_amount
            else:
                rec.billable = 0