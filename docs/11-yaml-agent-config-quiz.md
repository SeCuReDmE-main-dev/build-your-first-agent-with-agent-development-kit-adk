# Quiz — Agent configuration with YAML

Date : 12 septembre 2026  
Cours : [Build Your First Agent with Agent Development Kit (ADK)](https://www.skills.google/paths/3545/course_templates/1563/html_bundles/649843)  
Quiz : `649845` — Agent configuration with YAML  
Résultat observé : **100 %**

## Réponses et leçons

### 1. Créer un projet YAML

La commande correcte est :

```text
adk create --type=config my_agent
```

Elle crée la structure d’un agent configuré par fichier, notamment `root_agent.yaml`. Le point pédagogique est que le format de configuration devient une surface distincte du code d’exécution. La commande et le squelette ne prouvent cependant ni la qualité du comportement ni la préparation à la production.

### 2. Choisir YAML plutôt que Python

La configuration YAML est appropriée lorsque **des personnes qui ne programment pas doivent pouvoir modifier facilement le comportement de l’agent**. Cette réponse ne signifie pas que YAML remplace toute la logique applicative. Les outils, les callbacks, l’orchestration, la validation et les intégrations peuvent toujours nécessiter du code.

## Application au contexte Synthia

L’utilisateur veut surtout appliquer cette leçon pour préconfigurer et améliorer Synthia, un système public existant avec des éléments plithogéniques, neutrosophiques et de mémoire taxonomique. Le quiz ne justifie pas une adoption générique de Google ADK et ne transforme pas Synthia en agent ADK.

Le principe transférable est une frontière de conception : rendre les rôles, identités, descriptions, instructions et contrats simples relisibles dans une configuration humaine; garder la logique exécutable, les outils, la mémoire spécialisée et la taxonomie dans les couches qui les portent déjà; laisser l’état runtime et les handoffs dans leur propre couche. Une telle configuration pourrait faciliter une préconfiguration prudente de Synthia et une revue par des collaborateurs non programmeurs, mais seulement après inspection du système réel.

La présence de concepts plithogéniques, neutrosophiques ou taxonomiques impose de préserver leur sémantique et leur provenance. Il ne faut pas les aplatir dans un YAML générique ni déduire qu’un fichier déclaratif améliore automatiquement la mémoire, le raisonnement ou l’efficacité du contexte. Toute extraction devrait être évaluée avec les tests et les appelants existants.

## Limites et prochaine étape

Le score de 100 % établit la réussite de ce quiz précis. Il ne démontre pas une migration, une amélioration de Synthia, une compatibilité avec ADK, une sécurité de configuration ou un gain de tokens. La note locale de Synthia demeure une orientation pour une analyse future; elle n’autorise aucune chirurgie.

Prochaine étape pédagogique : examiner la structure actuelle de Synthia en lecture seule et dresser une carte de trois couches — configuration lisible, logique exécutable, état runtime — avant de proposer la moindre modification.

## Résumé en cinq lignes

1. Le quiz YAML est réussi à 100 %.
2. `adk create --type=config my_agent` crée un projet d’agent configuré par YAML.
3. YAML est utile quand des non-programmeurs doivent modifier facilement le comportement.
4. Pour Synthia, il s’agit d’un principe de préconfiguration, pas d’une adoption automatique de Google ADK.
5. La prochaine action est d’analyser Synthia en lecture seule avant toute chirurgie.

