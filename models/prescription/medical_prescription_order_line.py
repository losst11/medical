# -*- coding: utf-8 -*-

from odoo import fields, models

class MedicalPrescriptionOrderLine(models.Model):
    _name = 'medical.prescription.order.line'
    _inherit = ['abstract.medical.medication']
    _inherits = {'medical.patient.medication': 'medical_medication_id'}
    _rec_name = 'medical_medication_id'

    prescription_order_id = fields.Many2one(
        comodel_name='medical.prescription.order',
        string='Prescription Order', ondelete='cascade')
    medical_medication_id = fields.Many2one(
        comodel_name='medical.patient.medication', string='Medication',
        required=True, ondelete='cascade')
    is_substitutable = fields.Boolean()
    qty = fields.Float(string='Quantity')
