from odoo import fields, api, models,_


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    loyalty_program_id = fields.Many2one('loyalty.program', string = "Program Name")

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _get_default_product_id(self):
        domain = [('name', 'ilike', "coupon")]
        product_id = self.env['product.product'].search(domain,limit=1)
        if product_id:
            return product_id.id
        return False

    
    loyalty_program_id = fields.Many2one('loyalty.program', string = "Program Name")
    product_id = fields.Many2one(
        comodel_name='product.product',
        string="Product",
        change_default=True, ondelete='restrict', check_company=True, index='btree_not_null',
        domain="[('sale_ok', '=', True), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",default=_get_default_product_id)
