# -*- coding: utf-8 -*-
from odoo import http

# class SphMis(http.Controller):
#     @http.route('/sph_mis/sph_mis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sph_mis/sph_mis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sph_mis.listing', {
#             'root': '/sph_mis/sph_mis',
#             'objects': http.request.env['sph_mis.sph_mis'].search([]),
#         })

#     @http.route('/sph_mis/sph_mis/objects/<model("sph_mis.sph_mis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sph_mis.object', {
#             'object': obj
#         })