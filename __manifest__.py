{
    'name': 'Algolia Search Integration',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Integrate Algolia Search with Odoo eCommerce',
    'sequence': 10,
    'license': 'LGPL-3',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/search_results_view.xml',
        'views/analytics_dashboard_view.xml',
        'wizard/views/algolia_config_wizard_view.xml',
        'data/algolia_integration_data.xml',
        'static/src/xml/search_templates.xml',
        'static/description/index.html',
    ],
    'demo': [],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_frontend': [
            'static/src/js/search_integration.js',
            'static/src/css/search_styles.css',
        ],
    },
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'images': ['static/description/banner.png'],
    'description': """
Algolia Search Integration
=========================
This module integrates Algolia search engine with Odoo eCommerce to enhance search capabilities.
    """,
}