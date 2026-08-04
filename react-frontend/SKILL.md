---
name: react-frontend
description: "Stack et conventions frontend React officielles du Groupe NEO. TOUJOURS utiliser ce skill dès que la tâche touche au frontend : créer un nouveau projet ou composant React, une page, un hook, du styling Tailwind, un appel API depuis le client, ou une refonte UI. Trigger pour : 'nouveau projet', 'nouvelle app', 'composant React', 'page React', 'frontend', 'UI', 'Tailwind', 'Vite', 'refonte', 'dashboard client', 'portail'. Référence : versions de winwin-v2 + architecture de boom-contact."
---

# React Frontend — Groupe NEO

## Stack de référence (obligatoire pour tout NOUVEAU projet)

- React 19 + TypeScript strict — AUCUN fichier .js/.jsx dans src/. Zéro exception.
- Vite 6+ (pas de Next.js sauf besoin SSR/SEO explicite et validé)
- Tailwind CSS 4
- État serveur : @tanstack/react-query v5
- API : tRPC 11 si backend Node/TypeScript. REST + React Query si backend Flask/Python (tRPC ne fonctionne PAS avec Python).
- Icônes : lucide-react

## Architecture (modèle : boom-contact)

```
client/src/
  components/   # priorité : composants réutilisables D'ABORD
  pages/        # pages MINCES : composition de composants, pas de logique métier
  hooks/        # logique réutilisable (useX)
  services/     # appels API, clients externes
  lib/          # utilitaires purs
  i18n/         # si multilingue (FR par défaut)
```

Règles :
- Une page > 200 lignes = extraire des composants. Les pages composent, elles n'implémentent pas.
- Un composant = un fichier = une responsabilité.
- Pas d'abstraction pour du code à usage unique (YAGNI).

## Charte Groupe NEO

- Couleurs : `--accent: #3176A6` (bleu), `--sb-bg: #1a2332` (navy), fond `#f0f4f8`
- Fonts : Outfit (UI) + JetBrains Mono (données/code)
- Définir en variables CSS dans index.css, référencées dans la config Tailwind. Jamais de couleurs hex en dur dans les composants.

## Sécurité frontend (non négociable)

- JAMAIS de clé API, token, URL de base de données ou secret dans le code client, ni dans les fichiers VITE_* exposés au bundle (rappel : incident VITE_KNOWLEDGE_KEY juraitax).
- JAMAIS de credentials réels dans CONTEXT.md, SUIVI.md, DEPLOY.md ou tout .md — placeholders uniquement (voir skill varlock).
- Pas de .env commité. Vérifier .gitignore avant le premier commit.
- Pas de console.log en production (build check).

## Repos legacy — NE PAS imiter

- swissrh frontend : mélange JS/JSX à migrer, pas un modèle.
- immo-cool : Next.js 15, cas particulier, ne pas généraliser.
- wolf-saas : Vite 5 / Tailwind 3, versions gelées, ne pas copier.
- winwin-v2 pages/ : pages monolithiques historiques — suivre son package.json, pas sa structure de pages.

## Nouveaux projets : checklist de démarrage

1. `npm create vite@latest -- --template react-ts`
2. TypeScript strict: true, noUncheckedIndexedAccess: true
3. Tailwind 4 + variables charte NEO
4. Structure de dossiers ci-dessus créée vide dès le départ
5. .gitignore vérifié (.env, node_modules, dist)
6. Sentry initialisé dès le jour 1
7. RÈGLE ABSOLUE NEO : ne jamais casser une route existante ; vérifier le build avant de valider ; checker les logs après chaque deploy (Infomaniak en priorité, Railway sinon — voir skills infomaniak / deploy-checklist).
