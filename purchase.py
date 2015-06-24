from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
import math
from math import modf


class SevillaPurchaseRequisition(models.Model):
	_inherit = "purchase.requisition"

	STATUS_SELECTION = [
		('draft', 'New'),
		('head', 'Unit Head'),
		('custodian', 'Asset Warehouse Custodian'),
		('purchasing', 'Purchasing'),
	]

	def draft_status(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'status': 'draft'}, context=context)

	def submit_head(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'status': 'head'}, context=context)

	def submit_custodian(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'status': 'custodian'}, context=context)

	def submit_purchasing(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'status': 'purchasing'}, context=context)

	purpose = fields.Char(string="Purpose")
	status = fields.Selection(STATUS_SELECTION, string='Status', readonly=True, track_visibility='onchange', help='Info', select=True)
	code_id = fields.Many2one('sevilla.company.purchase', string='Company Type')#,
	dest_location = fields.Char(string='Destination Location')

	_defaults ={
		'status' : 'draft',
	}
	

class SevillaPurchaseRequisitionLine(models.Model):
	_inherit = "purchase.requisition.line"

	

	@api.one
	@api.depends('product_qty', 'amount')
	def compute_total(self):
		for x in self:
			x.total_amount = self.product_qty * self.amount


	@api.multi
	def onchange_product_id(self, product_id, product_uom_id):
		value = {'product_uom_id' : ''}
		if product_id:
			prod = self.env['product.product'].browse(product_id)
			value = {'product_uom_id':prod.uom_id,'product_qty':0.0, 'amount':prod.standard_price}
		return {'value': value}


	date_last = fields.Date(string="Date Last Requested")
	qty_surrendered = fields.Float(string="Qty Surrendered")
	unit_price = fields.Float(string="Unit Price")
	forecasted_qty = fields.Float(related='product_id.virtual_available', readonly=True, string="Forecasted Qty")
	actual_qty = fields.Float(related='product_id.qty_available', readonly=True, string="Actual Qty")
	amount = fields.Float(related='product_id.standard_price', string="Cost Price", readonly=True,)
	total_amount = fields.Float(string='Total', digits=dp.get_precision('Account'), store=True, readonly=True, compute='compute_total')
	
	
class SevillaCompanyConfig(models.Model):
	_name = "sevilla.company.purchase"

	name = fields.Char(string="Company Name", required=True)
	code = fields.Char(string="Company Code", required=True)
	_rec_name = 'code'


class SevillaPurchaseOrder(models.Model):
	_inherit = "purchase.order"

	terms_cond = fields.Text(string='Terms and Condition')


