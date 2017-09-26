# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteEventQuestions(http.Controller):
#     @http.route('/website_event_questions/website_event_questions/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_event_questions/website_event_questions/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_event_questions.listing', {
#             'root': '/website_event_questions/website_event_questions',
#             'objects': http.request.env['website_event_questions.website_event_questions'].search([]),
#         })

#     @http.route('/website_event_questions/website_event_questions/objects/<model("website_event_questions.website_event_questions"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_event_questions.object', {
#             'object': obj
#         })

# @api.onchange('amount', 'unit_price')
# def _onchange_price(self):
#     # set auto-changing field
#     self.price = self.amount * self.unit_price
#     # Can optionally return a warning and domains
#     return {
#         'warning': {
#             'title': "Something bad happened",
#             'message': "It was very bad indeed",
#         }
#     }