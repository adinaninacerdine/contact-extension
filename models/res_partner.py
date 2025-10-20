# models/res_partner.py
# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    region = fields.Selection(
        selection='_get_region_selection',
        string='Région',
        help='Région/Préfecture du contact'
    )
    
    @api.model
    def _get_region_selection(self):
        """Retourne toutes les régions possibles pour les trois îles"""
        return [
            # Ngazidja (Grande Comore) - 8 préfectures
            ('bambao', 'Bambao'),
            ('hambou', 'Hambou'),
            ('mbadjini', 'Mbadjini'),
            ('domba', 'Domba'),
            ('dimani', 'Dimani'),
            ('oichili', 'Oichili'),
            ('hamahamet', 'Hamahamet'),
            ('mboinkou', 'Mboinkou'),
            ('mitsamihouli', 'Mitsamihouli'),
            ('mboude', 'Mboudé'),
            ('hamanvou', 'Hamanvou'),
            ('itsandra', 'Itsandra'),
            
            # Ndzuani (Anjouan) - 5 préfectures
            ('mutsamudu', 'Mutsamudu'),
            ('ouani', 'Ouani'),
            ('domoni', 'Domoni'),
            ('mremani', 'Mrémani'),
            ('sima', 'Sima'),
            
            # Mwali (Mohéli) - 3 préfectures
            ('fomboni', 'Fomboni'),
            ('nioumachoua', 'Nioumachoua'),
            ('djando', 'Djando'),
        ]
    
    @api.onchange('state_id')
    def _onchange_state_region(self):
        """Réinitialise la région quand l'état change"""
        if self.state_id:
            # Réinitialise la région pour forcer une nouvelle sélection
            self.region = False