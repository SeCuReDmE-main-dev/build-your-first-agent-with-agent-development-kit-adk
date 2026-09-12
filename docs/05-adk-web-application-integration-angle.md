# Intégrer un agent ADK dans une application web

Date : 12 septembre 2026  
Cours : [Build Your First Agent with Agent Development Kit (ADK)](https://www.skills.google/paths/3545/course_templates/1563/html_bundles/649837)  
Angle étudié : appel HTTP au serveur ADK local depuis une application web

## Leçon

La page montre qu’un agent ADK peut être appelé par HTTP depuis une application. L’application web fournit l’interface et le contexte de l’utilisateur; le serveur ADK reçoit la requête, exécute l’agent et renvoie une réponse structurée. Cette séparation permet à un companion de side-panel d’utiliser un agent sans placer la logique du modèle directement dans le code de l’interface.

L’appel `curl` présenté par le cours est une preuve de communication avec un endpoint de développement. Il montre le chemin application → serveur ADK → agent → réponse. Il ne constitue pas à lui seul une API publique, une authentification complète, une gestion de sessions multi-utilisateurs ou un déploiement en production.

## Application à SecuredMe Education

Pour un side-panel de SecuredMe Education ou d’AlgoQuest, le navigateur pourrait envoyer une demande bornée au backend ADK. La requête devrait identifier la session utilisateur, l’objectif pédagogique courant et le contexte minimal autorisé. La réponse pourrait contenir l’explication, la prochaine question ou une action proposée. Le panneau conserve ainsi une porte humaine tandis que l’agent fournit le raisonnement et le guidage.

Le handoff vers un autre LLM ou companion doit préserver le contrat utile : rôle du personnage, objectif, état vérifié, sources, outils autorisés, actions déjà réalisées et prochaine étape. Un simple texte de conversation n’établit pas la provenance ni les permissions. Les identifiants `user/session` doivent rester des références contrôlées; aucune donnée privée d’apprenant ne doit être ajoutée à un exemple ou à un log de formation.

## Local et production

Le serveur ADK local lié à `127.0.0.1` sert à apprendre, inspecter et tester le flux. Il ne doit pas être décrit comme une infrastructure de production. Une version destinée à des utilisateurs demanderait au minimum une conception séparée de l’authentification, de l’autorisation par outil, de l’isolation des sessions, de la gestion des erreurs, de la limitation de débit, du coût, de la journalisation minimale et de l’évaluation. Ces sujets ne sont pas démontrés par l’appel HTTP du cours et ne sont pas ajoutés implicitement ici.

Le secret du fournisseur doit rester côté serveur dans l’environnement local ou géré. Il ne doit jamais être placé dans le JavaScript du navigateur, dans une commande copiée dans un rapport, dans un dépôt ou dans les données envoyées à un LLM tiers. Le point important pour l’apprentissage est donc la frontière de l’endpoint, pas la distribution de la clé.

## Limites et expérience pédagogique

Le test `curl` valide la connectivité et le format du parcours lorsque la réponse est observée. Il ne mesure pas encore la qualité pédagogique, la continuité après interruption, la fidélité d’un CCP, la sécurité d’une session ou le comportement sous plusieurs utilisateurs. Il ne prouve pas non plus qu’un side-panel réel est intégré à SecuredMe Education.

La prochaine expérience doit rester locale et sans donnée privée : appeler le même agent avec un identifiant de session fictif et une question pédagogique simple, puis noter le statut HTTP, la forme de la réponse, la durée et la présence d’une prochaine étape compréhensible. Comparer ensuite une requête sans contexte à une requête contenant un petit handoff structuré. Cette comparaison prépare l’étude CCP sans prétendre fournir une preuve de production.

## Résumé en cinq lignes

1. Une application web peut appeler un agent ADK par un endpoint HTTP.
2. Le side-panel garde l’interface humaine; le serveur ADK porte l’exécution de l’agent.
3. Un handoff utile transmet rôle, objectif, état, provenance, outils autorisés et prochaine action.
4. `127.0.0.1` et `curl` démontrent un parcours local de développement, pas un déploiement production.
5. La prochaine preuve est un appel local avec session fictive et comparaison d’un contexte simple avec un handoff structuré.

## Prochaine action pédagogique

Exécuter un appel HTTP local contrôlé avec `user_id` et `session_id` fictifs, observer la réponse ADK et consigner uniquement le statut, la durée et la structure non sensible de la réponse.

