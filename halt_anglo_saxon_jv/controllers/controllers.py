# -*- coding: utf-8 -*-
# from odoo import http


# class HaltAngloSaxonJv(http.Controller):
#     @http.route('/halt_anglo_saxon_jv/halt_anglo_saxon_jv/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/halt_anglo_saxon_jv/halt_anglo_saxon_jv/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('halt_anglo_saxon_jv.listing', {
#             'root': '/halt_anglo_saxon_jv/halt_anglo_saxon_jv',
#             'objects': http.request.env['halt_anglo_saxon_jv.halt_anglo_saxon_jv'].search([]),
#         })

#     @http.route('/halt_anglo_saxon_jv/halt_anglo_saxon_jv/objects/<model("halt_anglo_saxon_jv.halt_anglo_saxon_jv"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('halt_anglo_saxon_jv.object', {
#             'object': obj
#         })
