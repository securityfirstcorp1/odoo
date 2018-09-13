# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    seq_line_no = fields.Char('SO-Line NO', help="10 sol-line 1 and 20 sol-line 2, etc.....")
