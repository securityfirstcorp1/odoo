# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    next_line_no = fields.Integer('Sequence Number', help="10 sol-line 1 and 20 sol-line 2, etc.....", default=1, copy=False)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    seq_line_no = fields.Char('Sequence', help="10 and 20 , etc.....")

    @api.model
    def create(self, values):
        line = super(SaleOrderLine, self).create(values)
        line.seq_line_no = line.sequence*line.order_id.next_line_no
        line.order_id.next_line_no = line.order_id.next_line_no+1
        return line

    @api.multi
    def _prepare_invoice_line(self, qty):
        self.ensure_one()
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        res['seq_line_no'] = self.seq_line_no
        return res
