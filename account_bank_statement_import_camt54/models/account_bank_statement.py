# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models


class AccountBankStatement(models.Model):

    _inherit = 'account.bank.statement'

    _sql_constraints = [
        ('name', 'unique(name)', "Bank statement must be unique")
    ]
