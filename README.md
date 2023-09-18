# GESTION DE RÉSERVATION DES BILLETS D'UN ÉVÉNEMENT

1 - INTRODUCTION

Le système de gestion d'événements est une application développée dans le but de faciliter la gestion complète des événements, des participants et des billets associés. Cette application offre des fonctionnalités telles que la création, la modification et la suppression d'événements, l'enregistrement des participants ainsi que la gestion des billets vendus. Son objectif principal est de simplifier et d'optimiser l'organisation des événements en automatisant les processus d'inscription, de paiement et de suivi des données des participants. Grâce à cette application, les organisateurs d'événements pourront gérer efficacement toutes les facettes de leurs événements, améliorant ainsi l'expérience des participants et garantissant le bon déroulement de chaque événement.

2 - HYPOTHÈSE

Dans le cadre de ce projet de système de gestion d'événements, nous supposons que l'application sera utilisée principalement par des organisateurs d'événements pour gérer des événements de différentes natures tels que des conférences, des concerts ou des expositions.
Les opérations effectuées se concentrent principalement sur les opérations CRUD (Create, Read, Update, Delete) pour les entités principales : Événement, Participant et Billet. Voici un aperçu des opérations CRUD associées à chaque entité :
Événement :

Create : Créer un nouvel événement en spécifiant son nom, sa date, son lieu, sa description et sa capacité.
Read : Afficher les détails d'un événement existant, y compris son nom, sa date, son lieu, sa description et sa capacité.
Update : Mettre à jour les informations d'un événement existant, telles que son nom, sa date, son lieu, sa description ou sa capacité.
Delete : Supprimer un événement existant, y compris toutes les informations associées telles que les participants et les billets liés.
Participant :

Create : Enregistrer les détails d'un nouveau participant, tels que son nom, son adresse e-mail, son numéro de téléphone et son adresse.
Read : Afficher les informations d'un participant existant, y compris son nom, son adresse e-mail, son numéro de téléphone, son adresse et sa date d'inscription.
Update : Mettre à jour les informations d'un participant existant, telles que son nom, son adresse e-mail, son numéro de téléphone ou son adresse
Delete : Supprimer un participant existant, ainsi que toutes les données associées telles que les billets achetés.
Billet :

Create : Générer un nouveau billet en spécifiant son type, son prix, sa disponibilité, son numéro de série et l'événement auquel il est associé.
Read : Afficher les détails d'un billet existant, y compris son type, son prix, sa disponibilité, son numéro de série, l'événement auquel il est associé et le participant qui l'a acheté.
Update : Mettre à jour les informations d'un billet existant, telles que son type, son prix, sa disponibilité ou son numéro de série.
Delete : Supprimer un billet existant, ainsi que toutes les données associées.
Ces opérations CRUD permettent aux utilisateurs de gérer efficacement les événements, les participants et les billets, en créant de nouvelles entrées, en consultant les informations existantes, en mettant à jour les données et en supprimant les enregistrements selon les besoins.

3 - MATÉRIELS UTILISÉS :
Ordinateur : MacBook Pro 2020 m1
Logiciel : Anaconda-Navigator (Spyder), MySQL Community
Langage de programmation : Python, Sql
Interface graphique : Tkinter

4 - PROCÉDURE
- Analyse des besoins : Comprendre les exigences du système en termes de fonctionnalités et de contraintes. Définir les objectifs du projet et les fonctionnalités à implémenter.
- Conception de la base de données : Conception de la structure de la base de données en identifiant les entités (Événement, Participant, Billet) et leurs attributs. Définition des relations entre les entités, telles que la référence de l'événement dans les billets et la référence du participant dans les billets.
Configuration de l'environnement de développement : Installation Python, Tkinter et MySQL sur le système. Configuration l'accés l'accès à la base de données en utilisant des bibliothèques Python appropriées (comme MySQL Connector).
- Développement de l'application : Utilisation de Python et Tkinter pour créer l'interface utilisateur. Conception de la fenêtre principale, des formulaires et des boutons pour afficher et saisir les données des événements, des participants et des billets. Implémentation des fonctionnalités CRUD (Create, Read, Update, Delete) pour chaque entité en utilisant les requêtes SQL appropriées pour interagir avec la base de données MySQL.
- Implémentation des fonctionnalités spécifiques : Déployer les fonctionnalités spécifiques du projet, telles que la recherche d'événements, l'affichage du nombre d'événements, etc. Assurer la validation des données saisies par les utilisateurs et gérer d'éventuelles erreurs.
- Tests et débogage : Phase des tests pour vérifier les fonctionnalités de l'application. Identification et correction des erreurs, des bugs et des problèmes de logique.

5 - STRUCTURE DU CODE
Le projet se compose de deux fichiers principaux : classes.py et reservation_billet_evenement.py.

Le fichier classes.py contient la définition des classes suivantes : Evenement, Billet, Participant, et GestionBilletEvenementDB. Chacune de ces classes est dédiée à une fonction spécifique du projet.

La classe Evenement englobe les attributs et les méthodes nécessaires pour la gestion des événements, y compris des requêtes SQL pour interagir avec la base de données.

La classe Billet est chargée de la gestion des billets, avec ses attributs et méthodes associés, notamment des requêtes SQL pour interagir avec la base de données.

La classe Participant prend en charge la gestion des participants, avec des attributs et méthodes appropriés, incluant des requêtes SQL pour la base de données.

Quant à la classe GestionBilletEvenementDB, elle se charge de la création de la base de données et des tables associées si elles n'existent pas déjà. Elle offre également des méthodes pour établir et fermer la connexion à la base de données MySQL. Ces méthodes sont utilisées par les trois autres classes pour interagir avec la base de données.

Le fichier reservation_billet_evenement.py contient la classe Application, qui occupe une position centrale en connectant l'interface graphique élaborée avec Tkinter au programme Python. Elle facilite l'interaction entre l'utilisateur et les différentes fonctionnalités du projet.

6 - UTILISATION
Pour exécuter le code, il est nécessaire de fournir les paramètres de connexion à la base de données dans la méthode "_get_db_connection" du fichier classes.py. Cette méthode se situe comme suit :

À la ligne 31 pour la classe Evenement.
À la ligne 135 pour la classe Participant.
À la ligne 290 pour la classe Billet.

Il est essentiel de spécifier ces paramètres de connexion correctement pour que le programme puisse interagir avec la base de données MySQL.



