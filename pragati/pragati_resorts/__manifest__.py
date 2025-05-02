{
    'name':'loyalty_inherit',
    'summary':"""inherit loyalty wizard""",
    'depends':['base','loyalty','sale'],
    'data':['views/views.xml',
    'views/sale_inherit_views.xml',
            'wizard/inherit_loyalty_views.xml',
            # 'reports/inherit_loyalty_report_template.xml',
            # 'security/ir.model.access.csv',
            ],
}