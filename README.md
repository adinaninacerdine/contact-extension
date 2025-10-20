# Contact Extension - Module Odoo

Module d'extension pour les contacts Odoo avec support des régions des Comores.

## Modules inclus

### contact_region
Ajoute un champ région dynamique pour les contacts des Comores, avec sélection automatique selon l'île (état) choisie.

#### Fonctionnalités
- Sélection dynamique des régions selon l'état
- Support pour les trois îles : Ngazidja, Ndzuani, Mwali
- Filtrage et recherche par région

## Installation

1. Cloner ce dépôt dans votre dossier addons Odoo :
```bash
cd /chemin/vers/odoo/custom-addons
git clone https://github.com/adinaninacerdine/contact-extension.git
```

2. Redémarrer le serveur Odoo

3. Activer le mode développeur dans Odoo

4. Aller dans Apps → Mettre à jour la liste des applications

5. Rechercher et installer le module "Contact Region Comores"

## Configuration requise

- Odoo 18.0
- Module base
- Module contacts

## Licence

LGPL-3