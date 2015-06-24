from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
import math
from math import modf


class SevillaProduct(models.Model):
	_inherit = "product.template"

	#Additional fields
	classification_id = fields.Many2one('sevilla.classification')
	gen_description = fields.Char(string="Generic Description")

	tag_id = fields.Many2many('sevilla.assigned.unit','product_template_rel','product_template_col','assigned_unit_col')



class SevillaClassification(models.Model):
	_name = "sevilla.classification"

	#Additional field for configuration of Classification
	name = fields.Char(string='Classification')


class SevillaAssignedUnit(models.Model):
	_name = "sevilla.assigned.unit"

	name = fields.Char(string='Code')
	#description = fields.Char(string='Description')
