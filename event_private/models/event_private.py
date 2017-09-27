# -*- coding: utf-8 -*-

from odoo import models, fields

class EventPrivate(models.Model):
    _inherit = 'event.event'
    privateStatus = fields.Boolean(string="Private")
    shortUrl = fields.Char(string="Short url")