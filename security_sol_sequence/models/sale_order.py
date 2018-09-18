# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    next_line_no = fields.Integer('Sequence Number', help="10 sol-line 1 and 20 sol-line 2, etc.....", default=1, copy=False)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    @api.depends('order_id.amount_untaxed')
    def _compute_sol_line_sequence(self):
        for sol in self:
            if not sol.seq_line_no:
                sol.seq_line_no = max(sol.order_id.order_line.mapped('seq_line_no')) + 10

    seq_line_no = fields.Integer(string='Item', store=True, readonly=True, compute="_compute_sol_line_sequence", help="Sequencial item number for order lines (10, 20, 30, 40, etc.....)")


    @api.multi
    def _prepare_invoice_line(self, qty):
        self.ensure_one()
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        res['seq_line_no'] = str(self.seq_line_no)
        return res
