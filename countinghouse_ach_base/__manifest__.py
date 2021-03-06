# -*- coding: utf-8 -*-
# Copyright 2018 Thinkwell Designs <dave@thinkwelldesigns.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Localizations for North American Banking & Financials',
    'summary': 'Add fields required for North American Banking & Financials',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Thinkwell Designs',
    'website': 'https://github.com/thinkwelltwd/countinghouse',
    'category': 'Banking addons',
    'depends': [
        'account_payment_order',
    ],
    'data': [
        'views/account_banking_mandate.xml',
        'views/account_invoice.xml',
        'views/res_bank.xml',
        'views/res_company.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
}
