{
    'name': 'Sevilla Candle Factory, Inc.',
    'category': 'Specific Industry Applications',
    'summary': 'Sevilla Candle Factory, Inc.',
    'version': '0.1',
    'description': """


Sevilla Candle Factory, Inc.
====================================
Sevilla Candle Factory, Inc. Customizations



        """,
    'author': 'Toolkit',
    'depends': [
        'base', 'l10n_ph', 'product', 'purchase_requisition', 'hr', 'sale', 'purchase', 'pentaho_reports',

    ],
    'demo': [
    ],
    'data': [
        
        'res_partner_view.xml',
        'product_view.xml',
        'purchase_view.xml',
        'sale_view.xml',
        'invoice_view.xml',
        'report/report.xml',

    ],
    'qweb': [

    ],
    'installable': True,
}