# Claude Skills NEO — North Star canonique

Status: CANONICAL PRODUCT CONTRACT  
Owner: Claude Skills NEO / Groupe NEO  
Scope: reusable AI/development skills governance

## North Star

Claude Skills NEO doit être la **bibliothèque gouvernée de compétences réutilisables du Groupe NEO** qui rend les travaux assistés par IA plus sûrs, plus rapides, plus reproductibles et plus cohérents entre les produits, sans exposer de secret ni créer de doctrine parallèle.

Promesse :

> **Une capacité transverse utile ne doit être réinventée dans chaque projet ; une compétence non fiable ne doit pas être propagée à toute la flotte.**

## Invariants

- sécurité et provenance avant commodité ;
- aucun secret/token dans les bundles, exemples ou historiques ;
- versions et sources traçables ;
- une skill ne remplace pas l'autorité métier du produit ;
- les instructions doivent être exécutables, testables et maintenables ;
- réutiliser > améliorer > connecter > créer.

## Critères vérifiables

### NS-01 — Catalogue canonique
Le dépôt expose un inventaire unique et lisible des skills approuvées.

### NS-02 — Identité unique
Chaque skill possède un nom, un objectif et un périmètre non ambigus.

### NS-03 — Provenance
Chaque skill tierce conserve la source/provenance nécessaire pour audit et mise à jour.

### NS-04 — Version maîtrisée
Les versions ou révisions significatives sont traçables afin d'éviter une dérive silencieuse.

### NS-05 — Installation reproductible
Une skill peut être installée/chargée selon une procédure claire et reproductible.

### NS-06 — Contrat d'usage
Chaque skill indique quand l'utiliser, quand ne pas l'utiliser, ses préconditions et ses effets.

### NS-07 — Zéro secret
Aucun token, mot de passe, clé API ou secret utilisateur n'est versionné ni exposé par les skills.

### NS-08 — Sécurité de l'exécution
Les skills impliquant des mutations, déploiements, paiements ou données sensibles imposent des garde-fous appropriés.

### NS-09 — Séparation des autorités
Une skill transverse ne devient jamais une seconde source de vérité métier, readiness, infrastructure ou sécurité d'un produit.

### NS-10 — Tests / vérification
Les skills critiques ont une méthode de vérification, tests ou checklist permettant de détecter une régression.

### NS-11 — Compatibilité flotte
Les skills communes sont utilisables sur les environnements/outils NEO visés sans chemins privés ou hypothèses non documentées.

### NS-12 — Documentation concise et actionnable
Le point d'entrée de chaque skill permet à un agent de l'utiliser correctement sans contexte oral caché.

### NS-13 — Dépréciation contrôlée
Une skill remplacée est explicitement dépréciée/archivée et ne subsiste pas comme autorité concurrente.

### NS-14 — Maintenance
Les dépendances, APIs ou pratiques externes susceptibles d'évoluer peuvent être identifiées et mises à jour sans réécrire tout le catalogue.

### NS-15 — Réutilisation mesurable
Les skills doivent réduire la duplication ou améliorer de manière démontrable sécurité, qualité, vitesse ou cohérence sur au moins un workflow NEO réel.

### NS-16 — Gouvernance des skills personnelles
Les bundles personnels NEO peuvent être utilisés sans mémoriser ni exposer leurs secrets ; les connecteurs/variables d'environnement sont préférés.

### NS-17 — Atomicité des changements
Les évolutions du catalogue sont petites, révisables et n'altèrent pas silencieusement plusieurs skills sans raison.

### NS-18 — Definition of 100%
100 % signifie que NS-01 à NS-17 applicables sont PROVEN avec inventaire, provenance, contrôles sécurité, usage réel et preuves de non-régression. La simple présence de fichiers ne suffit pas.

## Progression

Ledger canonique : `docs/PROGRESS.md`.
