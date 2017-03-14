# -*- coding: utf-8 -*-

from odoo import fields, models

class MedicalLab(models.Model):
    _name = "medical.lab"
    _description = "Medical Labs"

    name = fields.Char(
        string='ID',
        size=128,
        required=True,
        default=lambda s: s.env['ir.sequence'].next_by_code(
            'medical.lab',
        ),
        help='Unique identifier for lab.',
    )
    test_type_id = fields.Many2one(
        string='Test Type',
        comodel_name='medical.test.type',
        help='Lab test type.',
    )
    physician_id = fields.Many2one(
        string='Pathologist',
        comodel_name='medical.physician',
        help='Pathologist that performed the exam.',
    )
    request_physician_id = fields.Many2one(
        string='Requesting Physician',
        comodel_name='medical.physician',
        help='Physician that requested the exam.',
    )
    date_request = fields.Datetime(
        string='Date Requested',
        default=lambda s: fields.Datetime.now(),
    )
    date_perform = fields.Datetime(
        string='Date of Analysis',
        default=lambda s: fields.Datetime.now(),
    )
    date_receive = fields.Datetime(
        string='Received Date',
        default=lambda s: fields.Datetime.now(),
    )
    result_ids = fields.One2many(
        string='Test Results',
        comodel_name='medical.lab.test.result',
        inverse_name='lab_id',
    )
    diagnosis_ids = fields.Many2many(
        string='Diagnoses',
        comodel_name='medical.pathology',
        help='Diagnosed pathologies as a result of this lab.',
    )
    notes = fields.Text(
        string='Additional Notes',
    )

    # visit_id = fields.Many2one(comodel_name='medical.visit', string='Visit', ondelete='cascade', index=True, copy=False)
    hospitalization_id = fields.Many2one(comodel_name='medical.hospitalization', string='Hospitalization', ondelete='cascade', index=True, copy=False)

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'The test ID code must be unique'),
    ]
