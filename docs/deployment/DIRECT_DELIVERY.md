# Livraison directe — catalogue Claude Skills NEO

## Nature du dépôt

`O-N-2950/claude-skills` est une bibliothèque de compétences réutilisables. Sa North Star gouverne la provenance, les versions, la sécurité d'exécution et les preuves d'usage. Ce dépôt ne contient pas d'application web, de base, de serveur, de configuration Railway/Jelastic, de domaine client, ni de route `/health`. L'absence de runtime dans l'arbre inspecté ne constitue pas une certification des installations consommatrices.

Inspection : 12.11.2026 à 06:07:27 (Europe/Zurich ; 05:07:27 UTC) ; base `dev@fa91bb9c06de0662886fa90521389bde13696e28`, arbre `809734b9977c39dd858df59de46a0899044c016e`. Les 30 chemins `*/SKILL.md` existent ; le README actuel annonce encore 19 skills. La PR [no 3](https://github.com/O-N-2950/claude-skills/pull/3) propose la correction du catalogue, mais n'est pas intégrée à cette base. La PR no 2 contient une ancienne diffusion de gouvernance ; aucune de ces PR ne doit remettre la version 1.3.0 après cette mise à jour.

## Application de la décision du 12.11.2026

Le bloc de politique 1.4.0, sa source et son empreinte sont copiés depuis NEO Core conformément à ADP-019. Les modifications vont directement sur `dev`, sans PR de diffusion. La North Star, les contenus des 30 skills et leurs règles de sécurité restent inchangés. On progresse toujours, on ne régresse jamais ; un contrôle non exécuté reste non prouvé.

La mise à jour des instructions sur `dev` ne démontre pas la mise à jour d'une installation Claude/agent consommatrice. Il ne faut donc pas annoncer une nouvelle version « en ligne » ni inventer `/health`, un canari web, des nœuds ou un domaine pour ce catalogue.

## Qualification d'une distribution future

Avant de distribuer des changements de skills, figer le SHA exact et disposer d'un arbre complet propre :

```bash
git status --porcelain=v1 --untracked-files=all
git rev-parse HEAD
git diff --check
```

Vérifier les instructions et le verrou épinglés, l'inventaire exhaustif, la provenance et les dépendances de chaque compétence affectée. Exécuter réellement les scénarios de chaque skill modifiée dans un environnement d'essai isolé, sans mutation des produits clients. Les compétences relatives à sécurité, données, paiements, facturation et envois réels nécessitent l'accord d'Olivier avant distribution affectant ces usages. Ne pas modifier ces compétences pour contourner les contrôles.

L'arbre initial inspecté ne fournit ni commande de build, ni suite exécutable pour les compétences, ni script d'installation ou de publication. Les contrôles de l'utilitaire de scellement couvrent le paquet ; la validation des marqueurs et des fichiers JSON couvre les instructions. Aucun de ces contrôles ne prouve le fonctionnement des 30 skills.

## Paquet, installation d'essai et restauration

L'utilitaire `scripts/deliver/artifact.py` permet de sceller les fichiers autorisés depuis le SHA exact et de vérifier le manifeste complet. Préparer le contenu complet de la distribution dans un dossier hors dépôt, après qualification ; puis utiliser :

```bash
python scripts/deliver/artifact.py seal --repo . --source /tmp/release --output /tmp/release.tar.gz
python scripts/deliver/artifact.py verify --archive /tmp/release.tar.gz --expected-sha "$RELEASE_SHA" --archive-sha256 "$ARCHIVE_SHA256" --manifest-sha256 "$MANIFEST_SHA256"
```

Ces commandes préparent et vérifient un paquet, sans l'installer. La vérification doit précéder l'installation dans un consommateur isolé et confirmer les versions réellement chargées. Une copie locale du catalogue n'établit pas cette dernière preuve.

**Distribution non exécutée :** aucun mécanisme de publication versionnée et aucun consommateur cible précis n'ont été vérifiés dans cette inspection. Aucun script de déploiement serveur fictif n'est ajouté. Le responsable des outils NEO doit identifier la cible de distribution et sa commande d'installation avant une première livraison.

Conserver la version installée précédemment et son manifeste. Le retour arrière consiste à réinstaller cette version identifiée, puis à vérifier la compétence réellement chargée et ses scénarios. Le mécanisme exact de restauration n'est pas encore prouvé ; cette documentation ne le déclare pas prêt.

La distribution ne doit comporter aucun secret, ni toucher des données réelles. Si un composant hébergé est introduit ultérieurement, il faut d'abord documenter sa cible réelle, ses accords sensibles, `/health` au SHA exact, ses tests et son canari ; les opérations Infomaniak passent alors par NEO Infomaniak MCP. Une modification `dev` seule n'autorise pas à redéployer les applications consommatrices.

Après distribution réellement vérifiée : consigner le SHA et l'heure de l'installation, les preuves et le retour arrière, réutiliser une seule PR `dev → main`, puis lancer NEO CI sur ce SHA. Les essais avec utilisateurs restent dans `docs/PROGRESS.md` sous « À prouver sur le terrain » ; aucun statut 100 % sans ces preuves.
