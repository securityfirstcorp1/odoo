# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Security SOL Sequence',
    'summary': 'Security SO-Line Sequence',
    'sequence': 100,
    'license': 'OEEL-1',
    'website': 'https://www.odoo.com',
    'version': '1.0',
    'author': 'Odoo Inc',
    'description': """
Security Sale Order Line Sequence
=================================
* Sale Order Line Sequence line 10 SO-Line 1, 20 SO-Line 2, etc ...
* Invoice Line Sequence when invoice created from Sale Order
* Sequence Line Show on PDF report
    """,
    'category': 'Custom Development',
    'depends': ['sale_management', 'account'],
    'data': [
        # Views
        'views/sale_order_views.xml',
        'views/account_invoice_views.xml',
        # Report
        'views/report_sale_order.xml',
        'views/report_invoice.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
