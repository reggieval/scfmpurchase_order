from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
import math
from math import modf


class SevillaResPartner(models.Model):
	_inherit = "res.partner"

	#Add tin and code (supplier and customer)
	tin = fields.Char(string='TIN Number')
	delivery_address = fields.Char(string='Delivery Address')
	territory_id = fields.Many2one('sevilla.territory')
	trade_name = fields.Char(string='Trade Name')

class SevillaTerritory(models.Model):
	_name = "sevilla.territory"

	#Additional field for configuration of Territory ID
	name = fields.Char(string='Territory ID')
