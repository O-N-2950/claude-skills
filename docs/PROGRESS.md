## 2026-11-12 — ADP-019 et distribution des compétences
- Utilitaire de scellement : **29 tests de contrat réussis** sur la version commune réellement exécutée et relue ; empreinte `artifact.py` `d6600e3862db736820c6c38f9ebd6d472ec503443f8ee95771c1864376d8235f`. Chaque copie installée est comparée à cette empreinte. Ces tests ne sont ni des tests navigateur ni une preuve de réception du paquet de cette application.


- Politique : bloc NEO 1.4.0 épinglé dans `AGENTS.md` et `CLAUDE.md`, verrou aligné sur `6c564f02f3b8ae1cae047653bc77bd6514e71725` et empreinte canonique `dbc9a0a0887b4ba6e4725064d3067ebc4c9d42653e6ad8fea9bf094b27d79a0b`. Règle locale enregistrée : « On progresse toujours, on ne régresse jamais ».
- Inspection : 12.11.2026 à 06:07:27 (Europe/Zurich ; 05:07:27 UTC). Base lue `dev@fa91bb9c06de0662886fa90521389bde13696e28`. `docs/NORTH_STAR.md`, README, arbre complet et PR ouvertes lus. Le dépôt est un catalogue de 30 compétences ; son README annonce encore 19, correction proposée dans la PR no 3 non intégrée à cette base.
- Préservation : aucun contenu de skill ni critère North Star modifié ; les compétences sensibles et leurs accords restent applicables. Aucun hébergeur, nœud, domaine ou API inventé pour une bibliothèque.
- Contrôles locaux : identité du bloc, marqueurs, source et empreinte, syntaxe du verrou et préservation des règles vérifiées sur les fichiers préparés. Aucun build, test applicatif ou scénario navigateur fourni par ce dépôt ; aucune réussite de ces contrôles non exécutés revendiquée.
- Distribution : **NON EFFECTUÉE**. SHA servi et heure de mise en ligne : **sans objet pour un catalogue sans service**. SHA réellement installé chez un consommateur : **UNKNOWN**. Aucun paquet publié ni application consommatrice redéployée.
- Blocages de distribution : mécanisme de publication versionnée, cible d'installation, scénarios isolés de skills et commande de restauration non identifiés. Responsable : mainteneur Claude Skills NEO / outils NEO. Reprise quand une distribution concrète et sa cible sont qualifiées ; la présente mise à jour documentaire ne certifie pas les 30 skills.
- Retour arrière : les commits Git précédents restent identifiables ; restauration de l'installation consommatrice **non prouvée**. Voir `docs/deployment/DIRECT_DELIVERY.md`.

### À prouver sur le terrain

| Quoi | Par qui | Quand |
| --- | --- | --- |
| Charger une version précisément identifiée et vérifier les compétences changées sur un workflow NEO autorisé | Mainteneur Claude Skills NEO et responsable du produit pilote | Après distribution isolée qualifiée ; avant généralisation |
| Prouver l'amélioration et l'absence de régression sur le workflow consommateur, avec trace de version | Responsable du produit pilote | Après essai ; avant 100 % North Star ou confirmation commerciale |

Les moyens techniques de distribution et de restauration manquants ne sont pas des preuves terrain différables.

## 2026-11-09 — Livraison progressive et preuves terrain

- Fait : décision d’Olivier du 09.11.2026 diffusée dans les instructions épinglées NEO Core 1.3.0.
- Règle historique remplacée le 12.11.2026 : l’attente de NEO CI avant livraison ne s’applique plus. ADP-019 exige les portes locales sur le SHA exact, le canari et les preuves de service ; NEO CI intervient après livraison. Les seuls essais terrain manquants restent différables.
- Contrôles maintenus avant livraison : sécurité, migrations, facturation, paiements et envois à de vrais clients. Aucun échec technique ni contrôle sensible manquant n’est reclassé en preuve terrain.
- Prouvé : présence du bloc et du pin contrôlée lors de la diffusion ; cela ne prouve ni la réception par les agents ni une nouvelle version en production.
- Propriétaire : responsable du produit et NEO Factory. Prochaine action : distinguer les blocages techniques des essais terrain, puis livrer le prochain candidat utile qualifié localement selon ADP-019.

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
| 4 | Version maîtrisée | UNKNOWN | Versions/pins à auditer |
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
