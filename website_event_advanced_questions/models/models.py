# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EventEvent(models.Model):
    """ Override Event model to add optional questions when buying tickets. """
    _inherit = 'event.event'

    question_ids = fields.One2many('event.question', 'event_id', 'Questions', copy=True)
    general_question_ids = fields.One2many('event.question', 'event_id', 'General Questions', domain=[('is_individual', '=', False)])
    specific_question_ids = fields.One2many('event.question', 'event_id', 'Specific Questions', domain=[('is_individual', '=', True)])

class EventQuestion(models.Model):
    _name = 'event.question'
    _rec_name = 'title'
    _order = 'sequence,id'
    # _inherits = 'event.question.datatype'

    title = fields.Char(required=True, translate=True)
    event_id = fields.Many2one('event.event', required=True, ondelete='cascade')
    sequence = fields.Integer(default=10)
    is_individual = fields.Boolean('Ask each attendee', default=True)
    description = fields.Text(translate=True)
    answer_ids = fields.One2many('event.answer', 'question_id', "Answers", required=True, copy=True)
    dataTypeValues = fields.Many2many('event.question.datatypevalue', string="EventQuestionDataTypeValue")
    isRequired = fields.Boolean('is required', default=True)
    
    # dataTypes = fields.Selection('_get_data_types', default='Text')
    dataTypes = fields.Selection('_get_data_types')

    @api.model
    def _get_data_types(self):
        datatypes = self.env['event.question.datatype'].search([])
        return [(datatype.name, datatype.value) for datatype in datatypes]

class EventQuestionDataType(models.Model):
    _name = 'event.question.datatype'
    name = fields.Char()
    value = fields.Char()

class EventQuestionDataTypeValue(models.Model):
    _name = 'event.question.datatypevalue'
    name = fields.Char()
    value = fields.Char()





class EventRegistrationAnswer(models.Model):
    ''' This m2m table has to be explicitly instanciated as we need unique ids
    in the reporting view event.question.report.

    This model is purely technical. '''

    _name = 'event.registration.answer'
    _table = 'event_registration_answer'

    event_answer_id = fields.Many2one('event.answer', required=True, ondelete='cascade')
    event_question_id = fields.Many2one('event.question', required=True, ondelete='cascade')
    event_registration_id = fields.Many2one('event.registration', required=True, ondelete='cascade')


class EventRegistration(models.Model):
    """ Store answers on attendees. """
    _inherit = 'event.registration'

    answer_ids = fields.Many2many('event.answer', 'event_registration_answer', string='Answers')
    question_ids = fields.Many2many('event.question', 'event_registration_question', string='Answers')

class EventAnswer(models.Model):
    _name = 'event.answer'
    _order = 'sequence,id'

    name = fields.Char('Answer', required=True, translate=True)
    question_id = fields.Many2one('event.question', required=True, ondelete='cascade')
    sequence = fields.Integer(default=10)