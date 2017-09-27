# -*- coding: utf-8 -*-
from odoo import fields, http, _
from odoo.addons.website.models.website import slug
from odoo.http import request

class WebsiteEventController(http.Controller):
    _inherit = 'event.event'
    
    # Render custom short url.
    @http.route(['/event/p/<string:shorturl>'], type='http', auth="public", website=True)
    def event_register_shorturl(self, shorturl, **post):
        events = request.env['event.event']
        event = events.search([['shortUrl', '=', shorturl]], limit=1)

        if event.state == 'done' or not event:
            return request.redirect("/event/%s" % slug(event))

        values = {
            'event': event,
            'main_object': event,
            'range': range,
        }
        return request.render("website_event.event_description_full", values)

        # values = {
        #     'event': event,
        #     'main_object': event,
        #     'range': range,
        #     'registrable': event._is_event_registrable()
        # }
        # return request.render("website_event.event_description_full", values)