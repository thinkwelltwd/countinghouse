# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID


def update_bank_journals(cr, registry):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        journals = env['account.journal'].search([('type', '=', 'bank')])
        ach_dd = env.ref('account_banking_ach_direct_debit.ach_direct_debit')
        if ach_dd:
            journals.write({
                'inbound_payment_method_ids': [(4, ach_dd.id)],
            })
    return
