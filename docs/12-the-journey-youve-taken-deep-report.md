# The journey you’ve taken — rapport approfondi et pré-conclusion

Date : 12 septembre 2026  
Cours : [Build Your First Agent with Agent Development Kit (ADK)](https://www.skills.google/paths/3545)  
Page de synthèse : https://www.skills.google/paths/3545/course_templates/1563/html_bundles/649846  
Périmètre : consolidation de l’itinéraire du cours, de l’environnement local et des quatre angles SecuredMe, avec préparation de la recherche CCP.

## Comment lire ce rapport

La page `The journey you’ve taken` est une synthèse pédagogique du parcours. Elle relie quatre activités : configuration de l’environnement, compréhension du premier agent, méthodes d’exécution et configuration YAML. Ce rapport distingue trois niveaux : ce que la page enseigne; ce qui est observé dans le workspace local; et ce que nous proposons comme application ou expérience future.

Un quiz réussi, un notebook créé ou un serveur local disponible constitue une preuve bornée. Cela ne prouve pas une maîtrise autonome de tout ADK, une intégration SecuredMe, une mémoire persistante, un cache de contexte, une sécurité multi-utilisateur ou un déploiement de production.

## 1. Ce que le parcours a construit

### 1.1 Environment setup

Le premier module établit le chemin de base : Python, environnement virtuel, installation de `google-adk`, accès au modèle par clé API ou authentification Google Cloud, création du projet avec `adk create`, puis lancement par `adk web`. Le projet Python est organisé autour de `agent.py`, `__init__.py` et `.env`. Cette structure sépare le code de l’agent, le point d’entrée Python et les paramètres secrets de l’environnement.

La leçon est reproductible : un agent n’est pas seulement une instruction envoyée à un modèle; il dépend d’un runtime, d’un paquet installable, d’un identifiant, d’un modèle et d’une configuration d’accès. Le secret doit rester côté environnement. La page donne une procédure d’apprentissage, pas une politique complète de production.

### 1.2 Understanding your first agent

Le deuxième module clarifie les quatre paramètres visibles de l’agent : `model`, `name`, `description` et `instruction`, ainsi que la convention `root_agent`. `model` désigne le modèle appelé; `name` donne une identité technique; `description` explique la capacité à un routeur ou à d’autres agents; `instruction` guide le comportement de l’agent lui-même.

La personnalisation en tuteur de mathématiques montre la différence entre instancier un agent et lui donner une méthode. Le premier quiz de cette section a confirmé que `model` et `name` suffisent techniquement au constructeur évalué, tout en laissant l’instruction indispensable à un comportement utile, sûr et pédagogique. Le test par `adk web` rend la réponse inspectable, mais ne remplace pas une évaluation structurée.

### 1.3 Other ways to run your agent

Le troisième module élargit les surfaces d’exécution : `adk run` pour le terminal, `adk api_server` pour un service appelable par une application et l’exécution programmatique avec `Runner`, sessions, contenus, parties et boucle asynchrone. Le répertoire parent doit être distingué du répertoire de l’agent afin que le runtime charge le bon package.

La différence est utile pour SecuredMe : `adk web` aide au débogage humain; l’API permet à un side-panel ou à un backend de parler au serveur; le mode programmatique laisse une application ou un notebook contrôler la création de session, l’envoi du message et la collecte de la réponse. Ces commandes montrent trois surfaces d’un même agent, pas trois garanties de déploiement.

### 1.4 Agent configuration with YAML

Le quatrième module présente `adk create --type=config my_agent`, le fichier `root_agent.yaml`, le schéma de configuration et les champs `name`, `model`, `description` et `instruction`. Une instruction multilignes peut utiliser `instruction: |`. Le YAML peut rendre un rôle et un contrat comportemental lisibles par une personne qui ne programme pas.

Python demeure la couche appropriée pour des outils, callbacks, orchestration, intégrations ou comportements dynamiques. La page officielle ADK qualifie Agent Config d’expérimental et décrit des restrictions de modèles, de langages et d’outils. La décision YAML/Python dépend donc de la lisibilité et de la complexité du système; elle ne doit pas être prise par imitation du tutoriel.

## 2. Ce qui est opérationnel maintenant

L’inspection du 12 septembre établit les faits locaux suivants :

- le workspace est `C:\Users\jeans\adk-workspace`, sur la branche `main`;
- Python `3.11.9` et `google.adk` `2.9.0` sont disponibles dans `.venv311`;
- `my_first_agent/agent.py` définit un `root_agent` nommé `math_tutor_agent`, avec modèle, description et instruction de tutorat;
- `adk web` est servi localement sur `127.0.0.1:8000` et une vérification HTTP locale a répondu `200`;
- le notebook programmatique [2026-09-12-adk-programmatic-execution-colab.ipynb](../notebooks/2026-09-12-adk-programmatic-execution-colab.ipynb) existe dans `notebooks/` et une copie Drive a été déposée selon la trace du travail;
- les fichiers `.env`, `.adk`, environnements virtuels, caches et journaux restent exclus du suivi approprié; aucune valeur secrète n’est reproduite;
- la présence du runtime et de la réponse HTTP ne prouve pas une réponse Gemini validée, une session persistante, une intégration web complète ou une production managée.

Le workspace possède des changements non suivis ou locaux liés aux notes YAML précédentes. Ils appartiennent au travail en cours et ne sont ni nettoyés ni inclus dans une publication. Aucun commit ou push n’est effectué par ce rapport.

Les rapports `04` à `11` sont les traces intermédiaires de ce parcours. Ils ont chacun isolé un quiz, une méthode d’exécution, l’expérience Colab, l’intégration web ou le principe YAML. La présente note les compile et devient la synthèse canonique du module ADK; les traces courtes restent utiles comme preuves détaillées et ne sont pas supprimées.

## Corrections et incidents rencontrés

Le travail a aussi enseigné que le chemin d’exécution compte autant que le code. Sous PowerShell, l’environnement `.venv311` devait être sélectionné explicitement et le répertoire parent devait être distingué du dossier d’agent pour que la commande `adk` découvre le bon package. Le serveur a été borné à `127.0.0.1`; sa réponse HTTP locale a ensuite été vérifiée séparément de l’interface navigateur. Cette correction de procédure évite de présenter une page ouverte ou une commande lancée dans le mauvais dossier comme une preuve d’exécution.

Un autre incident a été un `503` amont lors de certaines demandes au modèle, alors que la structure ADK et le runtime local restaient disponibles. Ce signal correspond à une saturation ou indisponibilité temporaire du fournisseur; il ne doit pas être transformé en défaut du code de l’agent ni en preuve de qualité. La réponse opérationnelle est de conserver la configuration, retenter dans une fenêtre bornée, noter le statut sans copier de journal brut et séparer disponibilité du service, validité de l’installation et qualité de la réponse.

Ces incidents ont conduit à corriger la frontière de preuve : une commande proposée n’est pas une commande exécutée; un serveur qui répond n’est pas une réponse Gemini validée; un `503` n’est pas une régression locale; un import ou modèle ajusté doit être revalidé avec la version ADK effectivement installée.

## 3. Les références et ce qu’elles ajoutent

| Référence | Classification | Apport fiable | Ce qu’elle ne prouve pas |
|---|---|---|---|
| [ADK API Reference](https://adk.dev/api-reference/) | Documentation technique primaire | Carte des API Python, TypeScript, Go, Java, Kotlin, CLI, YAML et REST | Qu’un design SecuredMe ou Synthia soit compatible sans inspection |
| [ADK Python Quickstart](https://adk.dev/get-started/python/) | Documentation technique primaire | Python, venv, `pip install google-adk`, structure du projet, `root_agent`, `adk run` et `adk web` | Production, persistance, sécurité multi-utilisateur ou qualité pédagogique |
| [Agent Config](https://adk.dev/agents/config/) | Documentation technique primaire | YAML, `root_agent.yaml`, schéma, chargement programmatique, outils et sous-agents, limites expérimentales | Que YAML apporte automatiquement une économie de contexte ou une meilleure identité |
| [Gemini Enterprise Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) | Documentation produit Google Cloud | Positionne les surfaces gérées de la plateforme et leur contexte cloud | Qu’un prototype local soit prêt à être déployé ou facturé |
| [Codelab — Building AI Agents with ADK: The Foundation](https://codelabs.developers.google.com/devsite/codelabs/build-agents-with-adk-foundation) | Codelab Google | Parcours guidé pratique pour les fondations ADK | Une preuve indépendante de robustesse ou de compétence client |
| [Build an agent with ADK and Agents CLI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/quickstart-adk) | Documentation Google Cloud / quickstart | Pont entre ADK, Agents CLI et Agent Platform | Une décision de déploiement pour SecuredMe |
| [Communauté Google Cloud](https://discuss.google.dev/c/google-cloud/cloud-build-ai/cloud-agents/200) | Forum communautaire | Questions, retours et pratiques de la communauté | Une source normative; chaque conseil doit être vérifié contre la documentation |

Les titres communautaires visibles dans la page — vidéos de tutoriel, cours pratiques, articles sur Google Tasks, Cloud Shell, UI et déploiement — sont utiles comme pistes de lecture. Leurs URLs exactes n’ont pas toutes été vérifiées dans cette session; ils ne sont donc pas traités comme preuves primaires. L’article Medium [Your First ADK agent: Building a Google Tasks to-do manager](https://medium.com/google-cloud/your-first-adk-agent-building-a-google-tasks-to-do-manager-c3d4d2c317cd) est une ressource communautaire identifiable, utile pour un exemple d’outil et de workflow, mais il ne remplace pas les docs ADK.

## 4. Les quatre angles de travail

### Angle 1 — ADK, infrastructure d’agent et professionnalisation

Le parcours transforme une idée générale d’agent en chaîne de construction : environnement isolé, définition, exécution, session, interface et configuration. La compétence professionnelle à retenir est la capacité à décrire la frontière de chaque couche et à fournir une preuve adaptée à chaque affirmation.

Pour une offre client, « construire un agent » doit devenir un résultat borné : un rôle défini, un scénario, des outils autorisés, une session contrôlée, une mesure de réussite et une limite explicite. Le socle actuel permet une découverte et un prototype local. Il ne justifie pas encore une promesse de production, d’observabilité, de conformité ou de coût.

### Angle 2 — Synthia, handoff et séparation des couches

Le principe YAML est pertinent pour analyser Synthia sans présumer qu’elle doit utiliser Google ADK. Une future lecture peut chercher une séparation entre configuration lisible — identité, rôle, description, instruction, défauts sûrs —, logique exécutable — outils, callbacks, orchestration, validations — et état runtime — session, objectifs, handoffs, mémoire, références et données temporaires.

La note locale de référence est `Z:\SecuredMe Education suite\Synthia\_organisation\2026-09-12-adk-yaml-config-base-note.md`. Elle reste une note d’organisation et de principe. Le dépôt réel de Synthia ne doit pas être modifié par ce rapport. La prochaine étude devra lire les appelants et les tests avant de conclure qu’une configuration déclarative améliorerait la relecture, le handoff ou la maintenance.

### Angle 3 — CCP, context caching et efficacité

Le parcours fournit les primitives qui rendent une expérience CCP testable : agent identifiable, sessions, Runner, API, exécution programmatique et distinction entre configuration stable et contexte variable. Un CCP peut transmettre objectif, état vérifié, provenance, actions effectuées, questions ouvertes et prochaine action.

Il faut le distinguer d’un context cache fournisseur. Un paquet portable n’est pas un cache KV portable. Une réduction d’octets, de tokens ou de calculs ne représente pas le même résultat. La page ne fournit aucun chiffre qui autoriserait une promesse d’économie universelle. Une comparaison future doit mesurer fidélité de reprise, omissions, inventions, actions répétées, tokens, latence et coût, avec une référence simple.

### Angle 4 — Companion side-panel, rôle et continuité

Le side-panel peut choisir la surface d’exécution adaptée : `adk web` pour le diagnostic, HTTP pour une application, Runner pour un flux programmatique. Le companion doit recevoir un handoff explicite : rôle, objectif, état, sources, outils autorisés, action réalisée et prochaine étape.

La description de l’agent peut aider au routage; l’instruction guide son comportement. Cette séparation est utile pour garder Neuro, Qbit ou un autre companion cohérent sans confondre personnage, modèle et session. Elle ne garantit pas une identité stable entre LLM. L’apprenant doit toujours voir ce qui a été proposé, ce qui a été exécuté et ce qui reste à comprendre.

## 5. Activité de recherche repo pour CCP

### Pourquoi cette recherche découle de la page

La page de synthèse donne maintenant les primitives nécessaires pour poser une question appliquée : définition d’un agent, exécution web/terminal/API/programmatique, `Runner` et sessions, séparation YAML/Python et possibilité de bâtir une application agentique. Il devient raisonnable de chercher un dépôt où un paquet de continuité pourrait réduire une friction ou un contexte répétitif lourd. Il serait prématuré de choisir un dépôt uniquement parce que son nom contient « agent » ou « memory ».

### Objectif

Choisir un cas réel où un CCP ou un mécanisme de continuité analogue allège un handoff ou un side-panel companion sans salir le contexte, sans recopier toute l’histoire et sans transformer une hypothèse en fonctionnalité. La question de test est : un paquet de reprise explicite permet-il de poursuivre correctement une tâche après interruption ou changement d’agent, à un coût acceptable ?

### Critères de sélection

Le dépôt retenu devra présenter :

- une activité et un problème observables;
- un besoin de continuité de rôle, de session ou de handoff;
- un contexte répétitif suffisamment lourd pour que la friction soit mesurable;
- des agents, un side-panel, une orchestration ou un flux analogue;
- un coût de tokens, de délai, d’actions répétées ou de remise en contexte observable;
- un test local possible sans données privées ni dépense non autorisée;
- une séparation nette entre notes d’organisation et code;
- aucune situation de jugement, de gel ou de contribution en attente qui rendrait l’intervention inappropriée.

### Pistes à conserver sans décider

| Piste | Statut actuel | Garde-fou |
|---|---|---|
| `Z:\03_LABS_EXPERIMENTS\WebMCP-Hackathon-2026` | Piste et avertissement | Ne pas toucher si le dépôt est en jugement ou gelé; vérifier le statut avant toute action |
| `Z:\SecuredMe Education suite\algoquest-production-lake` | Candidat possible lié à l’éducation | Vérifier le besoin réel de continuité et les tests avant toute proposition |
| `Z:\SecuredMe Education suite\algoquest-ams-discovry-labs-module-` | Candidat possible lié aux labs | Rechercher un scénario de reprise mesurable et éviter les doublons |
| `Z:\SecuredMe Education suite\Synthia` | Lecture conceptuelle et organisation seulement | Ne pas modifier le code; utiliser `_organisation` pour les notes autorisées |
| anciens dépôts hackathon NeuUuR-o / ReaAaS-n | Historique d’apprentissage | Classifier les sources; ne pas en faire une cible automatique ni attribuer une intégration ADK absente |

### Sortie attendue

La recherche future doit produire une matrice courte `repo × valeur CCP × risque × effort × prochain test`, accompagnée de l’URL, de la licence, de l’état des mainteneurs, du problème observé, de l’équivalent natif, du point d’intégration et des limites. La décision peut conclure qu’un mécanisme existant suffit ou que CCP n’apporte pas de valeur. Cette conclusion serait un résultat valide.

La recherche est planifiée; elle n’est pas exécutée par ce rapport. Aucun dépôt n’est sélectionné, aucun code n’est modifié et aucun message de mainteneur n’est préparé.

## Traces locales intégrées

La synthèse s’appuie sur les rapports locaux suivants, traités comme des sources de travail et non recopiés bout à bout :

- `docs/04-understanding-first-agent-quiz.md` — quatre paramètres, distinction routage/comportement, quiz à 100 %;
- `docs/05-adk-web-application-integration-angle.md` — endpoint HTTP, side-panel, sessions et frontière local/production;
- `docs/06-programmatic-execution-colab.md` — `Runner`, `InMemorySessionService`, notebook et expérience Colab;
- `docs/07-three-deployment-methods-source-classification.md` — classification des trois surfaces d’exécution et de leurs limites;
- `docs/08-other-ways-run-agent-quiz.md` — `adk run` et `adk api_server`, quiz à 100 %;
- `docs/09-yaml-agent-config-two-ways.md` — exercice YAML Synthia et séparation configuration/code/runtime;
- `docs/10-two-ways-define-agents-synthia-principle.md` — principe de configuration lisible sans adoption présumée d’ADK;
- `docs/11-yaml-agent-config-quiz.md` — `adk create --type=config my_agent`, choix YAML pour les non-programmeurs, quiz à 100 %.

La cohérence entre ces traces est la suivante : le même agent peut être décrit, testé et appelé par plusieurs surfaces, mais son contrat de comportement, son contexte de session, ses secrets et son évaluation doivent rester séparés. Les scores établissent des réussites de quiz précis; ils ne remplacent pas les preuves runtime ni les tests d’intégration.

## Ce qui devrait être réutilisé pour SecuredMe Education

Réutiliser la séparation entre contrat stable et état variable. Définir un rôle de companion lisible, un objectif pédagogique unique, une action autorisée et un critère de réussite. Utiliser l’exécution programmatique pour les expériences contrôlées et HTTP seulement lorsque l’application possède un backend clairement borné. Garder les secrets côté serveur et les données d’apprenant hors des exemples, journaux et rapports.

Le meilleur premier scénario n’est pas un tuteur qui prétend tout faire. C’est une petite tâche : reprendre un exercice interrompu, rappeler le concept vérifié, poser une question de transfert et laisser l’apprenant produire sa propre réponse. La réussite se mesure par la continuité et l’apprentissage observables, pas par la longueur ou la fluidité de la sortie.

## Limites générales

Le cours est une formation Google Skills et ses pages peuvent évoluer. Les docs ADK et Agent Config sont versionnées indépendamment du workspace; les commandes et capacités doivent être revalidées lors d’une mise à jour. Le workspace local prouve un environnement et une surface d’exécution; il ne prouve pas les propriétés d’un service public.

Les éléments Synthia, CCP, side-panel et offre client sont des applications ou hypothèses de conception issues de notre travail. Ils ne sont pas des fonctionnalités ajoutées par le cours. Aucun résultat de recherche repo, gain de cache ou test multi-utilisateur n’est revendiqué ici.

## À retenir pour continuer aujourd’hui

Le parcours a fourni les briques pour passer d’un agent local à une application contrôlée : définition, plusieurs modes d’exécution, sessions, Runner et configuration lisible. Le workspace local permet déjà d’apprendre et de tester dans une frontière bornée. La prochaine décision utile concerne le scénario de continuité, pas le choix précipité d’un framework. Synthia doit d’abord être analysée par ses couches et ses tests, sans chirurgie. Pour CCP, comparer une référence simple à un paquet minimal et mesurer la fidélité avant le coût.
