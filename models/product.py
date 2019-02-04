# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Product(models.Model):
    _inherit = 'product.template'

    membership = fields.Boolean(help='Check if the product is eligible for membership.')
    membership_duration = fields.Integer('Membership Duration (Days)')

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        if self._context.get('product') == 'membership_product':
            if view_type == 'form':
                view_id = self.env.ref('membership.membership_products_form').id
            else:
                view_id = self.env.ref('membership.membership_products_tree').id
        return super(Product, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
