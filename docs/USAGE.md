# Catalogue commun et autorités

Le dépôt contient des compétences réutilisables ; NEO Core garde la doctrine,
NEO Factory la livraison et chaque produit ses règles métier. Un bundle n'est
ni un rôle global ni une permission d'accès aux données d'un autre produit.

Les identités, chemins et empreintes réelles sont dans `catalog.json`. Générer
par `python scripts/catalog.py`, contrôler par `python scripts/catalog.py --check`.
Les empreintes identifient les fichiers, **pas leur approbation ni leur sécurité**.
La provenance tierce et les licences restent à auditer compétence par compétence.

## Chargement

Épingler une révision Git revue et charger seulement la compétence nécessaire
à la tâche. La disponibilité d'une option d'import dépend du client utilisé ;
la présence de ce dépôt ne prouve aucune installation dans Claude ou ChatGPT.
Respecter les mécanismes de chargement propres au client et les règles locales.

## Priorité des règles opérationnelles

1. North Star, instructions et déployeur du produit courant.
2. Doctrine NEO Core épinglée, dont le flux développement `dev` → release
   certifiée → branche réelle de livraison.
3. Compétence spécifique applicable.

Les bundles historiques citent Railway, d'anciens tarifs, versions et cycles
Git. Vérifier les faits instables avec la source officielle et l'état actuel.
**La compétence `use-railway` ne choisit pas Railway comme hébergeur.** Infomaniak
reste la cible des produits qui l'ont déclaré ; la plateforme réelle prime.
La convention de tests reste NEO CI, hors GitHub Actions en panne de facturation.

Le registre NEO Core référence ce dépôt comme outil transverse réservé.
Les outils personnels ne se propagent pas implicitement à toute la flotte.
Ne pas modifier les bundles pour supprimer un contrôle obligatoire local.
