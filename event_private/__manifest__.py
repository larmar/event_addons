# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################
{
    'name': "Event Private",
    "version": "1.0",
    "author": "Linserv AB",
    "category": "Events",
    "summary": "Makes private events",
    "website": "www.linserv.se",
    "contributors": [],
    "license": "",
    "depends": ['base', 'website_event'],
    'description': """ 
    
        App makes private events
        
    """,
    "demo": [],
    "data": [
        'static/src/xml/assets.xml',
        'views/inherited_website_event.xml',
        'views/inherited_event.xml'
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    "auto_install": False,
}