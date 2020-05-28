# -*- coding: utf-8 -*-
# from odoo import http


# class OdooModuleTest(http.Controller):
#     @http.route('/odoo_module_test/odoo_module_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_module_test/odoo_module_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_module_test.listing', {
#             'root': '/odoo_module_test/odoo_module_test',
#             'objects': http.request.env['odoo_module_test.odoo_module_test'].search([]),
#         })

#     @http.route('/odoo_module_test/odoo_module_test/objects/<model("odoo_module_test.odoo_module_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_module_test.object', {
#             'object': obj
#         })
