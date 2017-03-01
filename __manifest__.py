# -*- coding: utf-8 -*-
{
    'name': "medical",

    'summary': """
        Medical    
    """,

    'description': """
        - Medical
        - Medical Hospital
        - Medical Medicament
        - Medical Medication
        - Medical Disease
        - Medical Prescription
        - Medical Laboratory
    """,

    'author': "Capstone Solutions Inc.",
    'website': "http://www.capstone.ph",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Medical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        # 'views/medical_sequence.xml',
        'data/ir_sequence_data.xml',
        'data/medicament/medical_medicament_drug_form_data.xml',
        'data/medicament/medical_medicament_drug_route_data.xml',
        'data/medication/medical_medication_dosage_data.xml',
        'views/product_product_view.xml',
        'views/res_partner_view.xml',
        'views/medical_physician_view.xml',
        'views/medical_patient_view.xml',
        'views/medical_appointment_view.xml',
        'views/medical_specialty_view.xml',
        'security/medical_security.xml',
        'views/medical_menu.xml',
        'views/hospital/medical_hospital_bed_view.xml',
        'views/hospital/medical_hospital_room_view.xml',
        'views/hospital/medical_hospital_zone_view.xml',
        'views/hospital/medical_hospital_or_view.xml',
        'views/hospital/medical_hospital_unit_view.xml',
        'views/hospital/medical_hospital_menu.xml',
        'views/medicament/medical_medicament_product.xml',
        'views/medicament/medical_medicament_view.xml',
        'views/medicament/medical_medicament_drug_form_view.xml',
        'views/medicament/medical_medicament_drug_route_view.xml',
        'views/medicament/medical_medicament_menu.xml',
        'views/medication/medical_medication_dosage_view.xml',
        'views/medication/medical_medication_template_view.xml',
        'views/medication/medical_medication_patient_medication_view.xml',
        'views/medication/medical_medication_patient_view.xml',
        'views/medication/medical_medication_menu.xml',
        'views/disease/medical_disease_pathology_group_view.xml',
        'views/disease/medical_disease_pathology_category_view.xml',
        'views/disease/medical_disease_pathology_view.xml',
        'views/disease/medical_disease_patient_disease_view.xml',
        'views/disease/medical_disease_patient_view.xml',
        'views/disease/medical_disease_menu.xml',
        'views/prescription/medical_prescription_order_view.xml',
        'views/prescription/medical_prescription_order_line_view.xml',
        'views/prescription/medical_prescription_menu.xml',
        'views/lab/medical_lab_test_type_view.xml',
        'views/lab/medical_lab_view.xml',
        'views/lab/medical_lab_patient_view.xml',
        'views/lab/medical_lab_medical_patient_view.xml',
        'views/lab/medical_lab_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
        'demo/physician_specialty.xml',
        # 'demo/medical_medicament_demo.xml',
        # 'demo/medical_patient_demo.xml',
        'demo/disease/medical_pathology_category_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}