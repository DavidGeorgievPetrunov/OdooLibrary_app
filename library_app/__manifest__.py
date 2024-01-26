# -*- coding: utf-8 -*-
{
    'name': "library_app",

    'summary': """
        Patatas
        """,

    'description': """
        Biblioteca libreria
    """,

    'author': "David Petrunov",
    'website': "None",

    'category': 'Services/Library',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        "security/library_security.xml",
        #"security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
    ],
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}
