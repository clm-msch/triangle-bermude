
![Logo](https://res.cloudinary.com/diurvm1bd/image/upload/v1702619141/unic-paris-logo-banner_msgi5m.png)
# Unic Paris

Introducing Unic Paris, a cutting-edge web application built using Svelte Kit that seamlessly integrates with the open data API provided by the city of Paris. This innovative project aims to empower users by offering a comprehensive platform to explore and discover a plethora of activities within the enchanting city of Paris.


## Tech Stack
Gestion du projet avec Git sur GitHub

**Client:** 

- SvelteKit avec Vite :
  
SvelteKit est une extension élégante de Svelte, le framework JavaScript innovant. Il a été conçu pour simplifier et accélérer le processus de développement des applications web. L'un de ses points forts réside dans sa structure organisée qui facilite la gestion de la navigation, des requêtes serveur, et d'autres aspects clés du développement. Ce framework propose un modèle de routage intelligent, simplifiant la création de pages dynamiques et réactives. De plus, SvelteKit intègre des fonctionnalités telles que le rendu côté serveur (SSR) et la génération de pages statiques, améliorant ainsi la performance et l'expérience utilisateur. En utilisant nativement les modules JavaScript et en offrant une architecture intuitive, SvelteKit représente une solution puissante et efficace pour le développement d'applications web modernes.

- TailwindCSS :
  
Tailwind CSS, c'est bien plus qu'un simple framework CSS, c'est une approche pragmatique du stylisme web. Plutôt que de fournir des composants prédéfinis, Tailwind propose une palette étendue de classes utilitaires qui vous permettent de créer un style personnalisé et cohérent sans jamais quitter votre fichier HTML. Cette approche "utility-first" offre une flexibilité remarquable, vous permettant de personnaliser rapidement et efficacement l'apparence de votre site. L'intégration de Tailwind facilite également la collaboration au sein des équipes de développement, car la base de classes est comprise de manière universelle. Avec des fonctionnalités telles que la purge automatique des styles inutilisés, Tailwind optimise la taille finale du fichier CSS. En somme, en adoptant Tailwind CSS, vous profitez d'une approche intuitive et efficace du stylisme web, favorisant la productivité et la maintenabilité de votre code.

- Déploiement avec Vercel :
  Le processus de déploiement sur Vercel est transparent et automatisé, avec des mises à jour en temps réel dès que vous poussez du code vers votre référentiel Git. De plus, Vercel offre des fonctionnalités telles que le pré-rendu automatique, la mise en cache intelligente et la gestion des environnements, garantissant une expérience utilisateur optimale.

- Lucide :
  Simple et efficace pour la mise en place des icones

**Server:** 

- Django:
  L'utilisation de Django et de Django Rest Framework (DRF) est justifiée par leur efficacité et leur robustesse dans le développement web, particulièrement dans la création d'applications basées sur une architecture RESTful. Django, en tant que framework de développement web en Python, offre une structure de projet bien définie, facilitant la gestion des bases de données, la gestion des utilisateurs, et la création d'interfaces administratives. Il favorise également la réutilisation du code et la rapidité de développement grâce à son principe de "convention plutôt que configuration". En intégrant DRF, le processus de création d'une API REST devient encore plus fluide. DRF offre des outils puissants pour la sérialisation des données, la gestion des autorisations, la gestion des vues basées sur les classes, et d'autres fonctionnalités qui simplifient le développement d'API RESTful de manière cohérente et sécurisée. Ainsi, l'utilisation conjointe de Django et DRF constitue une solution robuste pour le développement d'applications web modernes, offrant à la fois une structure solide côté serveur et une API RESTful flexible et bien documentée.

- Creation d'une API

- Base de données MySQL :
  Le recours à MySQL comme système de gestion de base de données est justifié par sa réputation d'efficacité, de fiabilité et de polyvalence. En tant que base de données relationnelle open-source, MySQL est largement utilisé dans l'industrie pour son excellente performance, sa gestion efficace des transactions, et sa capacité à gérer des charges de travail importantes. Sa compatibilité avec un large éventail de langages de programmation et de plates-formes en fait un choix flexible pour les développeurs. De plus, MySQL offre des fonctionnalités avancées telles que la réplication, la montée en charge horizontale, et un ensemble complet d'outils d'administration. Son engagement envers les normes SQL assure une portabilité des données, facilitant l'intégration avec d'autres systèmes. En résumé, MySQL constitue un choix judicieux en raison de ses performances solides, de sa flexibilité, et de son adoption généralisée dans l'industrie, faisant de lui un moteur de base de données fiable pour une variété d'applications.

- Déploiement avec AlwaysData :
  Le choix d'Alwaysdata pour l'hébergement repose sur plusieurs facteurs qui en font une solution attrayante et fiable. Tout d'abord, Alwaysdata propose une plateforme d'hébergement web qui se distingue par sa simplicité d'utilisation, avec une interface conviviale qui simplifie la gestion des serveurs et des applications. Son modèle de tarification flexible permet de s'adapter aux besoins spécifiques, offrant des ressources évolutives selon les exigences du projet. La diversité des langages de programmation pris en charge, ainsi que la facilité d'intégration avec des outils de développement courants, font d'Alwaysdata un choix polyvalent pour les développeurs. De plus, la stabilité et la performance des serveurs, associées à un support réactif, renforcent la confiance dans la disponibilité continue des applications hébergées. Enfin, Alwaysdata accorde une importance particulière à la sécurité, en mettant en place des mécanismes de protection avancés, ce qui en fait une solution complète et fiable pour l'hébergement de projets web.



## To-Do

**Client:**
- Création des composants ✅
- Creation du layout des pages ✅
- Faire le routing des pages ✅
- Connecter le front avec l'API ✅
- Déployer le Front sur Vercel ✅

**Server:**
- Création de l'API ✅
- Création des modèles de la base de données ✅
- Création des routes de l'API ✅
- Création de la base de données sur AlwaysData ✅
- Déployer l'API sur AlwaysData ✅


## BDD Schema

![Schema_BDD](https://i.ibb.co/9gxxh9P/schema-bdd.png)

## Commentaires

- Fabien :
  Avis : projet sympathique à faire, juste pas compréhensible d'utiliser une api pour faire une autre api
  Difficultés  : en front il n'y avait pas de difficultés en particulier, juste peut être trouver une map qui fonctionne avec sveltekit et typescript
  J'aurais aimé pouvoir faire un système de compte ou les gens peuvent liker des destinations par exemple

- Cyril :
  Avis : Projet assez complexe du fait de la tête des données récupérées et du peu de temps qu'on possédait cependant quand même assez cool et challengeant.
  Difficultés : Les 2 principales difficultés rencontrées ont été premièrement, la découverte de Django qui a été un petit peu longue mais très instructive et un vrai challenge et deuxièmement, le réarrangement des données qui a été long et compliqué.
  J'aurai juste aimé pouvoir faire en sorte de pouvoir récupérer tous les événements qui possèdent 1 ou plusieurs tags spécifié(s) dans la requête.

- Clément :
Avis : un bon défi surtout d'un point de vue temps, mais plutôt bonne organisation et répartition des tâches entre nous. Petite perte de temps sur l'UI, mais bon process sur le front-end avec Svelte qui nous a permis de très vite créer les composants.
Difficultés : malheureusement, Svelte s'est montré assez capricieux dans sa compatibilité avec les library de map et de carousel, ce qui a rendu le développement assez fastidieux.
J'aurais aimé permettre un filtrage beaucoup plus poussé avec chaque détails, ainsi qu'une page d'accueil plus poussée.
> by @scotty974 @ShuHado @clm-msch
