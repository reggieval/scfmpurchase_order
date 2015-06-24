from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
import math
from math import modf



class SevillaSaleOrder(models.Model):
	_inherit = "sale.order"

	po_number = fields.Char(string='PO #')
	trip_ticket = fields.Char(string='Trip Ticket #')
	total_case = fields.Float(string='Total Cases')
	ship_to = fields.Char(related='partner_id.delivery_address', required=True, string='Ship to', store=True)
	code_id = fields.Many2one('sevilla.company', string='Company Type')#,
	

class SevillaCompanyConfig(models.Model):
	_name = "sevilla.company"

	name = fields.Char(string="Company Name", required=True)
	code = fields.Char(string="Company Code", required=True)
	_rec_name = 'code'


class SevillaSaleOrderLine(models.Model):
	_inherit = "sale.order.line"

	discount_id = fields.Many2one('sevilla.discount.type', string='Type of Discount')


class SevillaDiscountType(models.Model):
	_name = "sevilla.discount.type"

	name = fields.Char(string='Type of Discount')
    