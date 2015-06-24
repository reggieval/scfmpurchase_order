from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
import math
from math import modf

class SevillaInvoice(models.Model):
	_inherit = "account.invoice"

	#Additional Fields for Customer + Supplier Invoice
	code_id = fields.Many2one('sevilla.company', string='Company Type')#,

	#Additional Fields for Customer Invoice
	scf_invoice_number = fields.Char(string='Invoice Number',
		default=False, copy=False, help="Manual Invoice Number")

	scf_dr_number = fields.Char(string='DR Number',
		default=False, copy=False, help="Manual DR Number")

	po_number = fields.Char(string='PO #')
	trip_ticket = fields.Char(string='Trip Ticket #')
	total_case = fields.Float(string='Total Cases')

	#Additional Fields for Supplier Invoice
	#TO ADD: pre-numbered, STC series, SCF series
	scf_voucher_number = fields.Char(string='Check Voucher Number',
		default=False, copy=False, help="Check Voucher Number")

	scf_petty_cash_voucher = fields.Char(string='Petty Cash Voucher',
		default=False, copy=False, help="Petty Cash Voucher Number")

	scf_cash_advance_number = fields.Char(string='Cash Advance Number',
		default=False, copy=False, help="Cash Advance Number")

	scf_receipt_counter = fields.Char(string='Receipt Counter',
		default=False, copy=False, help="Receipt Counter Number")

	scf_cash_voucher_number = fields.Char(string='Cash Voucher Number',
		default=False, copy=False, help="Cash Voucher Number")

class SevillaVoucher(models.Model):
	_inherit = "account.voucher"

	scf_voucher_number = fields.Char(string='Check Voucher Number',
		default=False, copy=False, help="Check Voucher Number")

	scf_petty_cash_voucher = fields.Char(string='Petty Cash Voucher',
		default=False, copy=False, help="Petty Cash Voucher Number")

	scf_cash_advance_number = fields.Char(string='Cash Advance Number',
		default=False, copy=False, help="Cash Advance Number")

	scf_receipt_counter = fields.Char(string='Receipt Counter',
		default=False, copy=False, help="Receipt Counter Number")

	scf_cash_voucher_number = fields.Char(string='Cash Voucher Number',
		default=False, copy=False, help="Cash Voucher Number")

	post_dated_check = fields.Char(string='Post-dated Check')