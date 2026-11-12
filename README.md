# 🧠 Claude Skills — Groupe NEO

> Skills Claude personnalisés pour tous les projets O-N-2950

**30 skills** couvrant sécurité, déploiement Railway, Stripe, PostgreSQL, tests, marketing.

---

## 🔴 Critiques (tous projets)

| Skill | Source | Utilité |
|-------|--------|---------|
| `systematic-debugging` | obra/superpowers | Root cause avant tout fix |
| `verification-before-completion` | obra/superpowers | Prouver avant de valider |
| `owasp-security` | agamm | OWASP Top10 2025 + ASVS 5.0 |
| `varlock` | wrsmith108 | Secrets jamais exposés dans sessions/logs/git |

## 🟠 Infrastructure

| Skill | Source | Projets cibles |
|-------|--------|----------------|
| `use-railway` | railwayapp OFFICIEL | Uniquement produits dont Railway est la plateforme vérifiée |
| `postgres` | sanjay3290 | winwin-v2, wolf-saas, swissrh, mekano |
| `postgres-best-practices` | supabase OFFICIEL | winwin-v2, provis |
| `webapp-testing` | anthropics OFFICIEL | immo-cool, peps-v2-pwa, wolf-saas |

## 🟡 Dev workflow

| Skill | Source | Projets cibles |
|-------|--------|----------------|
| `test-driven-development` | obra/superpowers | TOUS |
| `writing-plans` | obra/superpowers | TOUS (planification avant code) |
| `finishing-a-development-branch` | obra/superpowers | TOUS (workflow fin de branche) |

## 🟢 Paiements & Intégrations

| Skill | Source | Projets cibles |
|-------|--------|----------------|
| `stripe-best-practices` | stripe OFFICIEL | wolf-saas, provis, peps-v2-pwa |
| `stripe-upgrade` | stripe OFFICIEL | wolf-saas (migration SDK) |

## 🔵 Marketing & Growth

| Skill | Source | Projets cibles |
|-------|--------|----------------|
| `cold-email` | coreyhaines31 | wolf-saas, winwin-v2 |
| `pricing-strategy` | coreyhaines31 | wolf-saas, provis, juraitax |
| `referral-program` | coreyhaines31 | peps-v2-pwa, jvais |
| `seo-audit` | coreyhaines31 | immo-cool, juraitax, synergis-landing |
| `lead-research-assistant` | ComposioHQ | winwin-v2, pepssolutions |
| `invoice-organizer` | ComposioHQ | provis, winwin-v2 |

---

## Catalogue vérifiable et chargement

[Inventaire complet et empreintes](catalog.json) · [Contrat d’usage et autorités](docs/USAGE.md).

Le catalogue réel comporte **30 compétences** : la sélection ci-dessus n’est pas
exhaustive. Le chargement dépend du client ; aucune installation n’est inférée
de la présence du dépôt. Épingler une révision revue et charger le bundle utile.

```sh
python scripts/catalog.py
python scripts/catalog.py --check
```

Les empreintes vérifient l’inventaire, pas la sécurité ou la provenance des bundles.
La plateforme du produit, sa North Star et la doctrine NEO Core épinglée priment
sur les exemples historiques. Voir [PROGRESS.md](docs/PROGRESS.md).
