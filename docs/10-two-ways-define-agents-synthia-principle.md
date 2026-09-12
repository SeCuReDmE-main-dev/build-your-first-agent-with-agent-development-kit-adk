# Deux façons de définir un agent — principe pour une future analyse de Synthia

Date : 12 septembre 2026  
Cours : [Build Your First Agent with Agent Development Kit (ADK)](https://www.skills.google/paths/3545/course_templates/1563/html_bundles/649843)  
Source technique : [ADK Agent Config — Build an agent](https://adk.dev/agents/config/#build-an-agent)  
Portée : synthèse pédagogique; cette note ne décide pas d’adopter Google ADK pour Synthia.

## La distinction Python/YAML

La définition Python décrit l’agent dans du code exécutable. Elle convient lorsque la construction dépend de conditions dynamiques, d’outils, de callbacks, d’orchestration ou d’intégrations applicatives. Elle donne une grande liberté, mais mélange plus facilement la configuration lisible et la logique d’exécution si le projet n’établit pas de frontière claire.

La configuration YAML décrit l’agent dans un fichier déclaratif, généralement `root_agent.yaml`. La documentation ADK montre les champs `name`, `model`, `description` et `instruction`, avec un schéma JSON associé. Une instruction multilignes peut être écrite avec `instruction: |`, ce qui conserve une présentation lisible pour un rôle, des règles et une méthode de réponse. ADK peut charger cette configuration et instancier l’agent via `config_agent_utils.from_config(...)`.

Le YAML est adapté lorsque l’identité, la capacité annoncée et le contrat comportemental doivent être relus ou révisés rapidement par un humain. Python reste préférable pour les comportements qui nécessitent du code : outils, validation, état persistant, orchestration, callbacks et intégrations. Les deux couches peuvent coexister : YAML pour le contrat stable, code pour l’exécution.

## Champs et responsabilités

| Élément | Rôle | Couche naturelle |
|---|---|---|
| `name` | Identité technique de l’agent | YAML ou Python |
| `model` | Modèle appelé | YAML ou Python, selon la configuration d’exécution |
| `description` | Capacité lisible par un routeur ou un autre agent | Configuration déclarative |
| `instruction` | Règles et comportement attendus par l’agent | Configuration déclarative, souvent `instruction: |` pour plusieurs lignes |
| outils, callbacks, orchestration | Actions et logique exécutable | Python ou autre code autorisé |
| session, mémoire, handoff, CCP | État de fonctionnement et contexte variable | Runtime / application |

Cette séparation évite de confondre l’identité d’un agent avec son état de session. Elle permet aussi de vérifier qu’une instruction décrit un comportement attendu sans prétendre que ce comportement a été évalué simplement parce qu’il est écrit dans un fichier.

## Ce que cela suggère pour Synthia

La correction importante est que Synthia n’est pas un agent générique à inventer. C’est déjà un dépôt public avec une identité, une gouvernance, des lanes, des tests et un langage interne : contexte lexical, taxonomie mémoire, provenance, incertitude, `I -> I_system^S -> H_lex -> G_lex -> I_lexicon`, `T/I/F`, noyaux neutrosophiques, contradiction plithogénique, rough regions et revue humaine. Une configuration utile doit donc préserver cette structure au lieu de repartir d’une abstraction vide.

La note locale [2026-09-12-adk-yaml-config-base-note.md](Z:/SecuredMe%20Education%20suite/Synthia/_organisation/2026-09-12-adk-yaml-config-base-note.md) et le brouillon [2026-09-12-synthia-antigravity-handoff-config-draft.yaml](Z:/SecuredMe%20Education%20suite/Synthia/_organisation/2026-09-12-synthia-antigravity-handoff-config-draft.yaml) retiennent le principe suivant : une future chirurgie Synthia doit séparer la configuration lisible, la logique exécutable et l’état runtime, mais elle doit le faire à partir des conventions réelles de Synthia. La configuration peut porter identité, lane, rôle de handoff, frontières d’autorité, source policy et prochaine action vérifiable. Le code porte les pipelines, outils, callbacks, WebMCP, validations, kernels et gouvernance. Le runtime porte sessions, sources, paquets de revue, CCP, handoffs, mémoire et artefacts temporaires.

Cette leçon s’applique à Synthia comme principe d’architecture et de lisibilité. Elle ne signifie pas que Synthia doit utiliser Google ADK, convertir son système en ADK Agent Config ou migrer son code. Pour ce dossier, l’exercice sert surtout à préparer la façon dont Codex/OpenAI ou Antigravity/Gemini recevraient un handoff Synthia sans aplatir son modèle. La question utile devient : quelles parties stables du rôle Synthia doivent être visibles avant qu’un autre agent touche au repo ?

Pour un companion SecuredMe ou un handoff entre LLM, une telle séparation clarifie ce qui appartient à Synthia, ce qui appartient à l’application, et ce qui appartient à la session. Elle peut aider à construire un CCP plus compact : conserver le contrat stable comme référence et transmettre seulement l’objectif, l’état vérifié, la provenance, les blocages et la prochaine action. Aucun gain de tokens ou de latence n’est établi par la présence d’un YAML; il faudra le mesurer.

## Limites expérimentales d’ADK Agent Config

La documentation officielle qualifie Agent Config d’expérimental. Elle indique notamment un support actuel limité aux modèles Gemini, Python étant requis pour l’installation et le chargement de la configuration, ainsi que des restrictions de support pour certains outils et types d’agents. Les configurations peuvent être lancées par interface web, ligne de commande, serveur API ou code, mais cette possibilité ne constitue pas une preuve de production.

Ces limites comptent pour l’analyse comparative : un format déclaratif peut améliorer la revue humaine sans résoudre l’authentification, la persistance, l’isolation des sessions, l’évaluation, la sécurité ou le coût. Il faut également vérifier la version ADK et le schéma avant de réutiliser un exemple, car les capacités expérimentales peuvent évoluer.

## Résumé en cinq lignes

1. Python définit un agent avec une logique exécutable; YAML décrit un contrat déclaratif lisible.
2. `root_agent.yaml` peut porter `name`, `model`, `description` et `instruction: |` avec un schéma vérifiable.
3. YAML convient aux rôles et comportements stables; Python reste nécessaire pour outils, orchestration et intégrations dynamiques.
4. Pour Synthia, c’est un principe de handoff et de séparation configuration/code/runtime ancré dans son modèle réel, pas une décision d’adopter Google ADK.
5. Agent Config est expérimental et ne prouve ni production, ni mémoire, ni cache, ni sécurité, ni gain d’efficacité.

## Prochaine action future

Analyser d’abord la structure réelle de Synthia — lanes publiques, configuration, logique exécutable, état runtime, tests, appelants, WebMCP, document pipeline et gouvernance — puis décider s’il existe un bénéfice démontrable à extraire un contrat lisible pour les handoffs Codex/OpenAI et Antigravity/Gemini, sans lancer de chirurgie ni migration sur la seule base de cette leçon.
