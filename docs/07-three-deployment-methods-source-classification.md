# Three deployment methods — classification des sources

Date : 12 septembre 2026  
Cours : [Build Your First Agent with Agent Development Kit (ADK)](https://www.skills.google/paths/3545/course_templates/1563/html_bundles/649842)  
Activité : `Other ways to run your agent - Three deployment methods`  
Périmètre : comparaison pédagogique de `adk web`, du serveur API et de l’exécution programmatique Python.

## Trace du travail effectué

La troisième méthode, l’exécution programmatique avec Python, a été préparée dans le notebook local [2026-09-12-adk-programmatic-execution-colab.ipynb](../notebooks/2026-09-12-adk-programmatic-execution-colab.ipynb). Une copie a été déposée dans le dossier Drive fourni pour l’activité; les identifiants de fichier et de dossier sont conservés comme références opératoires dans la note précédente `docs/06-programmatic-execution-colab.md`, sans secret ni donnée d’apprenant.

Le notebook est un support d’apprentissage. Sa création et son dépôt ne démontrent pas un déploiement de production, une disponibilité continue, une authentification utilisateur ou une persistance des sessions.

## Classification des sources

| Source | Type | Utilité principale | Leçon | SecuredMe Education | CCP / efficacité du contexte | Limites |
|---|---|---|---|---|---|---|
| [Google Skills — activité](https://www.skills.google/paths/3545/course_templates/1563/html_bundles/649842) | Source de cours et navigation pédagogique | Présente les trois façons de lancer le premier agent et situe le choix de la troisième méthode | Un même agent peut être inspecté dans une interface, exposé par HTTP ou appelé depuis du code | Permet de choisir le point d’intégration selon le besoin du companion : débogage, endpoint ou contrôle applicatif | Aide à placer le contexte au bon niveau : session gérée par l’application, requête HTTP ou état Python; ne prouve aucun gain de tokens | La page de cours ne suffit pas à définir une architecture de production, des garanties de sécurité ou un contrat CCP |
| [ADK Python — Run your agent](https://adk.dev/get-started/python/#run-your-agent) | Documentation technique de démarrage, source primaire | Décrit le lancement local avec `adk web` et `adk run`, le chargement du package et la boucle de test | Le runtime local fournit une surface de développement pour observer et appeler un agent; le code de l’agent reste séparé de l’interface | Utile pour vérifier le comportement d’un companion avant de le relier à un panneau ou à un backend | Sert de référence simple pour comparer le contexte envoyé par l’interface et celui d’une session contrôlée; aucune compression ou mise en cache n’est fournie par défaut | ADK Web et `adk run` sont des surfaces de développement; la documentation ne constitue pas une preuve d’authentification, d’isolation multi-tenant ou de production |
| [ADK Agent Team tutorial](https://adk.dev/tutorials/agent-team/) | Tutoriel technique sur la composition d’agents | Montre comment organiser un agent d’équipe et déléguer vers des agents spécialisés | La description aide le routage et l’instruction guide le comportement de l’agent sélectionné; l’orchestration doit rester explicite | Peut inspirer une séparation entre tuteur, évaluateur et agent de handoff, avec outils et limites propres à chaque rôle | Rend nécessaire un CCP qui transporte l’objectif, l’état, la provenance et la prochaine action entre agents; transmettre tout l’historique serait coûteux et fragile | Un tutoriel d’équipe ne prouve pas une architecture éducative sûre, une mémoire durable, une réduction de coûts ou une identité stable entre modèles |

## Les trois méthodes en pratique

`adk web` fournit une interface de développement pratique pour charger l’agent, envoyer des messages et observer les événements. C’est le meilleur point d’entrée pour comprendre le comportement et repérer une erreur de configuration. Dans un side-panel, cette surface serait un outil interne de test, pas l’interface finale de l’apprenant.

`adk api_server` expose un parcours HTTP adapté à une application qui possède déjà son interface. Le navigateur ou le frontend envoie une requête au backend autorisé, lequel appelle l’agent. Cette méthode correspond directement au modèle companion side-panel → backend → ADK. L’endpoint doit garder les secrets côté serveur et appliquer ses propres contrôles de session; le simple fait qu’un endpoint réponde ne prouve pas ces contrôles.

L’exécution programmatique avec `Runner`, `InMemorySessionService`, `Content` et `Part` donne au code Python la maîtrise de la session et de la collecte de la réponse. C’est la méthode choisie pour le notebook Colab parce qu’elle rend l’expérience reproductible et permet de tester le comportement avant de construire une interface. `InMemorySessionService` est adapté à l’apprentissage et au prototype; il ne constitue pas une mémoire persistante pour une suite éducative multi-utilisateur.

## Relation au companion et au handoff

Les méthodes sont trois surfaces pour un même contrat d’agent. Le side-panel peut utiliser HTTP pour l’intégration, tandis qu’un notebook ou un test Python vérifie une session; `adk web` permet à l’humain de diagnostiquer. Un handoff vers un autre LLM ou companion devrait transmettre le rôle, l’objectif, l’état vérifié, la provenance, les outils autorisés et la prochaine action. Il ne devrait pas transmettre automatiquement des secrets, des journaux bruts ou tout l’historique.

Le tutoriel Agent Team ajoute une question de routage : quel agent est compétent pour l’étape courante ? La description de capacité peut aider le routeur, alors que l’instruction définit la conduite interne. Pour SecuredMe Education, cette distinction doit rester visible dans l’évaluation : un agent peut être bien sélectionné mais mal guidé, ou produire une réponse convaincante sans accomplir l’action pédagogique attendue.

## Relation au CCP et au contexte

Le choix de méthode ne crée pas automatiquement un CCP ni un context cache. Le CCP est le paquet portable de reprise; le cache est une réutilisation de calcul soumise aux règles du fournisseur. Pour une expérience contrôlée, comparer : (A) session native et contexte complet, (B) résumé court, (C) CCP minimal seulement si la perte de continuité justifie sa création. Mesurer reprise correcte, omissions, inventions, répétitions, tokens, latence et coût.

Le premier objectif est la fidélité, pas la réduction artificielle du texte. Les identifiants de session, les URLs, le code et les sources doivent rester valides. Le notebook et les exemples de cours ne contiennent aucune mesure permettant de conclure à une économie universelle ou à une latence garantie.

## Limites de portée

La classification décrit l’utilité pédagogique des sources observées. Elle ne transforme pas un endpoint local en déploiement production et ne conclut pas que l’architecture Agent Team convient automatiquement à SecuredMe Education. Les questions d’authentification, d’autorisation, d’isolation des apprenants, de persistance, de coûts, de surveillance et de reprise après panne restent des travaux distincts.

## Résumé en cinq lignes

1. Google Skills présente trois surfaces : interface `adk web`, serveur HTTP et exécution Python.
2. La documentation Python explique surtout le lancement et le test local de l’agent.
3. Le tutoriel Agent Team ajoute le routage et la délégation entre agents spécialisés.
4. Le notebook Colab rend la troisième méthode testable, mais ne constitue pas un déploiement production.
5. La prochaine preuve est une comparaison locale de session native, résumé et CCP minimal avec mesures de fidélité et d’effort.

