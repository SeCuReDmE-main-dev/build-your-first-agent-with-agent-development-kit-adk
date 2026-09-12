# Understanding your first agent — rapport du quiz

Date : 12 septembre 2026  
Cours : [Build Your First Agent with Agent Development Kit (ADK)](https://www.skills.google/paths/3545/course_templates/1563/html_bundles/649837)  
Section : `Understanding your first agent`  
Quiz : [Google Skills — 649841](https://www.skills.google/paths/3545/course_templates/1563/quizzes/649841)  
Résultat observé : **100 %**

## Ce que le quiz vérifie

Le quiz porte sur deux distinctions précises dans la définition d’un agent ADK. La première question demande quels paramètres sont requis pour créer un agent LLM fonctionnel : **le modèle (`model`) et le nom (`name`) uniquement**. La réponse doit être comprise dans le sens technique du constructeur : ces deux champs suffisent pour créer l’objet agent. Une instruction reste essentielle pour obtenir un comportement utile, sûr et prévisible, mais elle n’est pas classée comme paramètre techniquement requis par cette question.

La deuxième question demande la différence entre `description` et `instruction`. La correction est : **la description est lue par d’autres agents pour prendre des décisions de routage; l’instruction est lue par l’agent lui-même pour guider son comportement**.

Cette différence sépare deux contrats. `description` expose la capacité de l’agent à l’extérieur, afin qu’un orchestrateur ou un autre agent puisse décider si celui-ci est pertinent. `instruction` définit la conduite interne : objectif, méthode, niveau d’explication, limites et critères de réponse. Confondre les deux peut produire un agent correctement routable mais mal guidé, ou un agent bien instruit que l’orchestrateur ne sait pas sélectionner.

## Lecture dans le workspace local

Le dépôt respecte la séparation attendue par le cours : `my_first_agent/agent.py` contient le `root_agent`, l’environnement et les dépendances sont isolés, et les secrets restent dans `.env` sans être inclus dans cette note. Le code courant donne à l’agent le nom interne `math_tutor_agent`, une description orientée vers le tutorat mathématique et une instruction détaillée qui impose une explication progressive, la définition des symboles, des exemples et une courte vérification de compréhension.

Cette configuration illustre directement le quiz. Le nom et le modèle créent l’agent au niveau du constructeur. La description indique à un système de délégation dans quels cas le tutorat mathématique peut être pertinent. L’instruction transforme ensuite cet agent générique en tuteur avec une méthode et des limites pédagogiques. Cette note ne modifie pas `agent.py` et ne présente pas les outils, la mémoire, le CCP ou le cache comme déjà implémentés.

## Angle 1 — Formation Google/ADK et professionnalisation

Le score de 100 % documente la réussite de cette vérification accompagnée. L’apprentissage utile est plus précis que le score : construire un agent demande de connaître la différence entre le minimum syntaxique et le contrat de comportement. Dans une prestation, cette distinction aide à séparer le paramétrage de base, la conception du comportement, l’évaluation et la maintenance.

La leçon professionnelle est de pouvoir expliquer ce qui est requis pour démarrer et ce qui est requis pour livrer une solution fiable. `model` et `name` permettent l’instanciation; ils ne prouvent ni la qualité de la réponse, ni la pertinence métier, ni la sécurité. La description et l’instruction rendent ensuite le rôle observable et testable.

## Angle 2 — CCP et efficacité du contexte

La paire `description`/`instruction` offre une première séparation pour un paquet de continuité. La description stable peut servir de métadonnée de capacité lors de la sélection d’un agent. L’instruction stable peut être conservée comme contrat de comportement. L’objectif courant, l’état vérifié, les sources, les actions réalisées et la prochaine étape appartiennent au contexte variable d’une session et peuvent être transportés par un CCP.

Cette organisation peut réduire le contexte répété, mais aucune économie de tokens, de latence ou de coût n’est démontrée par le quiz. Un cache fournisseur réutilise un calcul selon ses propres règles; un CCP transporte une reprise portable. Il faudra mesurer séparément taille, tokens, fidélité de reprise, invalidation et coût avant de conclure qu’une représentation est plus efficace.

## Angle 3 — SecuredMe Education, companion side-panel et handoff

Pour un companion de side-panel, `description` et `instruction` peuvent devenir deux niveaux du handoff. Le routeur reçoit une capacité lisible : par exemple, « accompagne une activité de mathématiques de niveau défini ». Le companion reçoit son contrat interne : comment expliquer, quand demander une précision, quelles actions sont permises et comment signaler une limite.

Le handoff doit également transmettre l’état dynamique et sa provenance. Un nom de personnage ne suffit pas à garantir une identité cohérente entre modèles ou panneaux. Neuro, Qbit ou un tuteur doivent conserver un rôle, des outils autorisés et des limites explicites, tandis que le CCP porte la session en cours. L’apprenant doit pouvoir distinguer la recommandation du companion, l’action réellement exécutée et la compréhension qu’il a construite.

## Angle 4 — Article et study case du soir

Le quiz fournit une petite leçon exploitable pour l’article : un agent est à la fois une capacité adressable et un comportement guidé. La question de study case peut donc devenir : un contrat séparant routage, comportement et état de reprise réduit-il les erreurs de handoff dans un scénario réel ?

La première expérience doit comparer un mécanisme natif, un résumé simple et, seulement si nécessaire, un CCP minimal contenant objectif, état vérifié, références, actions déjà effectuées, questions ouvertes et prochaine action. Les critères sont la reprise correcte, les omissions, les inventions, les actions répétées, les tokens et le délai. Une telle preuve pourra soutenir une offre client bornée autour d’une continuité vérifiable; le score du quiz seul ne justifie pas une promesse de déploiement.

## Limites

Le résultat de 100 % établit la réussite de cette section. Il ne démontre pas une maîtrise autonome de tout ADK, ni l’implémentation d’outils, de mémoire, de sessions persistantes, de cache, de multi-agent ou de déploiement. Le sens de « requis » dans la première question est celui du constructeur technique utilisé par le quiz; dans un système réel, une instruction explicite est généralement nécessaire pour obtenir le comportement attendu.

Aucun secret, journal brut, contenu de `.env`, donnée privée ou information d’apprenant n’est reproduit ici. Aucun changement n’a été apporté à `my_first_agent/agent.py`.

## Résumé en cinq lignes

1. Le quiz de la section `Understanding your first agent` est réussi à 100 %.
2. Les paramètres techniquement requis sont `model` et `name`; l’instruction reste nécessaire pour le comportement utile.
3. `description` sert au routage par d’autres agents, tandis que `instruction` guide l’agent lui-même.
4. Cette séparation clarifie le companion side-panel et fournit une base pour distinguer contrat stable et état CCP variable.
5. La prochaine preuve est une expérience de handoff mesurée, avant toute conclusion sur l’efficacité du cache ou une offre client.

## Prochaines actions pédagogiques

1. Expliquer avec un exemple personnel la différence entre capacité routable, instruction interne et état de session.
2. Poursuivre le parcours ADK vers l’ingénierie du comportement, puis mémoire/état et outils.
3. Exécuter une conversation locale contrôlée et enregistrer seulement des métadonnées non sensibles.
4. Comparer une reprise native, un résumé et un CCP minimal sur le même scénario.
5. Relier les observations mesurées à l’article du soir en séparant faits, hypothèses et propositions commerciales.
