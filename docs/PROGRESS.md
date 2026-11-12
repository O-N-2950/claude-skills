## 2026-11-09 — Livraison progressive et preuves terrain

- Fait : décision d’Olivier du 09.11.2026 diffusée dans les instructions épinglées NEO Core 1.3.0.
- Règle : livrer une étape utile V1/V2/V3/V4/finale après NEO CI vert sur le SHA exact et contrôles applicables ; les seuls essais terrain manquants ne bloquent plus la livraison.
- Contrôles maintenus avant livraison : sécurité, migrations, facturation, paiements et envois à de vrais clients. Aucun échec technique ni contrôle sensible manquant n’est reclassé en preuve terrain.
- Prouvé : présence du bloc et du pin contrôlée lors de la diffusion ; cela ne prouve ni la réception par les agents ni une nouvelle version en production.
- Propriétaire : responsable du produit et NEO Factory. Prochaine action : distinguer les blocages techniques des essais terrain, puis livrer le prochain candidat utile certifié.

### À prouver sur le terrain

| Quoi | Par qui | Quand |
| --- | --- | --- |
| Inventorier les essais avec utilisateurs et preuves d’usage réel restant à réaliser pour cette application, sans les déclarer acquis | Responsable du produit | Après livraison de l’étape concernée ; avant toute déclaration 100 % North Star ou confirmation commerciale finale |

# Claude Skills NEO — PROGRESS

Source: `docs/NORTH_STAR.md`  
Rule: UNKNOWN remains UNKNOWN. PARTIAL does not count as attained.

| # | Critère | Statut | Preuve |
|---:|---|---|---|
| 1 | Catalogue canonique | PARTIAL | README inventorie 19 skills ; exhaustivité à certifier |
| 2 | Identité unique | PARTIAL | Catalogue nommé ; bundles à auditer |
| 3 | Provenance | PARTIAL | README référence plusieurs sources ; audit complet requis |
| 4 | Version maîtrisée | PARTIAL | Catalogue de 30 fichiers avec empreintes ; politique de versions et pins consommateurs à auditer |
| 5 | Installation reproductible | PARTIAL | Procédure GitHub indiquée ; smoke à certifier |
| 6 | Contrat d'usage | UNKNOWN | Audit de chaque skill requis |
| 7 | Zéro secret | UNKNOWN | Scan dépôt/bundles requis |
| 8 | Sécurité exécution | UNKNOWN | Audit skills mutantes requis |
| 9 | Séparation autorités | PARTIAL | Doctrine NEO ajoutée ; contrôle bundles requis |
| 10 | Tests / vérification | UNKNOWN | Inventaire tests/checklists requis |
| 11 | Compatibilité flotte | UNKNOWN | Validation sur workflows NEO requise |
| 12 | Documentation actionnable | PARTIAL | README catalogue présent ; entrypoints à auditer |
| 13 | Dépréciation contrôlée | UNKNOWN | Politique/archive à vérifier |
| 14 | Maintenance | UNKNOWN | Process update à prouver |
| 15 | Réutilisation mesurable | UNKNOWN | Cas réels/KPI requis |
| 16 | Gouvernance skills personnelles | PARTIAL | Doctrine connecteurs/env connue ; code à prouver |
| 17 | Atomicité changements | UNKNOWN | Historique PR/commits à auditer |
| 18 | Definition of 100% | INCOMPLETE | Dépend de NS-01 à NS-17 |

Updated: 2026-10-02


## Lot 05.11.2026 — inventaire réel et rattachement aux autorités

- 30 SKILL.md inventoriés, contre 19 annoncés dans l’ancien README.
- `catalog.json` contient chemins, tailles et SHA-256 ; le contrôleur détecte une
  modification de bundle non répercutée dans l’inventaire.
- `docs/USAGE.md` relie le catalogue aux autorités NEO Core, Factory et produit,
  limite Railway aux cibles vérifiées et ne revendique aucune installation client.
- T0 local : inventaire et empreintes vérifiés par `python scripts/catalog.py --check`.
- Aucun SKILL.md modifié ; provenance, licences, sécurité et usage réel restent
  à auditer. NS-01 PARTIAL, NS-04 PARTIAL (identité des fichiers seulement).
- Certification NEO CI et diffusion des modifications : à vérifier sur le SHA final.
