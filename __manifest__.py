# __manifest__.py
# -*- coding: utf-8 -*-
{
    'name': 'Contact Region Comores',
    'version': '18.0.1.0.0',
    'category': 'Contact',
    'summary': 'Ajoute un champ région dynamique pour les Comores',
    'description': """
        Ce module ajoute un champ région qui se remplit automatiquement 
        selon l'état sélectionné pour les trois îles des Comores
    """,
    'author': 'ADINANI Nacer-Dine',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}