#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ce fichier fait partie d'un projet de gestion de reservation des billets pour des evenement.
Il contient la définition des classes (Participant, BilletEvenement, et une classe qui gère la connexion à la base donnée 'GestionBilletEvenementDB') 

"""

# Importations des biblios nécessaires
import re
import mysql.connector
from datetime import datetime

class Evenement1:
    
    """
    Cette classe Evenement gère les opérations liées aux événements dans la base de données, 
    notamment l'ajout, la suppression, la modification et la récupération des événements. 
    Elle utilise la classe GestionBilletEvenementDB pour obtenir la connexion à la base de données.
    """  
    
    def __init__(self, nom_ev, date_ev, lieu_ev, description_ev, capacite_ev):
        self.nom_ev = nom_ev                    # Nom evenement
        self.date_ev = date_ev                  # Date evenement
        self.lieu_ev = lieu_ev                  # Lieu evenement
        self.description_ev = description_ev    # Description evenement
        self.capacite_ev = capacite_ev          # Capacité evenement
        
    # Méthode privée pour obtenir la connexion à la base de données
    def _get_db_connection(self):
        # Créez une instance de GestionBilletEvenementDB pour obtenir la connexion à la base de données
        db = GestionBilletEvenementDB(
            host="localhost",
            user="root",
            password="Stage2023",
            database="Reservation"
        )
        connection = db.get_connection()
        return db, connection
    
    # Méthode privée pour fermer la connexion à la base de données
    def _close_db_connection(self, db):
        db.close_connection()

    # Méthode pour ajouter un événement à la base de données
    def ajouter(self):
        mydb, connection = self._get_db_connection()
        query = "INSERT INTO evenement (nom_ev, date_ev, lieu_ev, description_ev, capacite_ev) VALUES (%s, %s, %s, %s, %s)"
        values = (self.nom_ev, self.date_ev, self.lieu_ev, self.description_ev, self.capacite_ev,)
        mycursor = connection.cursor()
        mycursor.execute(query, values)
        mycursor.close()

        # Fermez la connexion
        self._close_db_connection(mydb)

    # Méthode pour supprimer un événement de la base de données par son ID
    def supprimer(self, id_ev):
        mydb, connection = self._get_db_connection()
        query = "DELETE FROM evenement WHERE id_ev = %s"
        value = (id_ev,)
        mycursor = connection.cursor()
        mycursor.execute(query, value)
        mycursor.close()

        # Fermez la connexion
        self._close_db_connection(mydb)
        
    # Méthode pour modifier un événement dans la base de données
    def modifier(self, nouveau_nom, nouvelle_date, nouveau_lieu, nouvelle_description, nouvelle_capacite, id_ev):
        mydb, connection = self._get_db_connection()
        query = "UPDATE evenement SET nom_ev = %s, date_ev = %s, lieu_ev = %s, description_ev = %s, capacite_ev = %s WHERE id_ev = %s"
        values = (nouveau_nom, nouvelle_date, nouveau_lieu, nouvelle_description, nouvelle_capacite, id_ev)
        mycursor = connection.cursor()
        mycursor.execute(query, values)
        mycursor.close()

        # Fermez la connexion
        self._close_db_connection(mydb)

    # Méthode pour rechercher un événement par son ID
    def rechercher_par_id(self, id_evenement):
        mydb, connection = self._get_db_connection()
        query = "SELECT nom_ev FROM evenement WHERE id_ev = %s"
        value = (id_evenement,)
        mycursor = connection.cursor()
        mycursor.execute(query, value)
        result = mycursor.fetchone()
        mycursor.close()
        
        return result

    # Méthode statique pour rechercher un événement par son nom
    def rechercher_par_nom(self,nom):
        mydb, connection = self._get_db_connection()
        query = "SELECT * FROM evenement WHERE nom_ev LIKE %s"
        value = (nom,)
        mycursor = connection.cursor()
        mycursor.execute(query, value)
        result = mycursor.fetchall()
        mycursor.close()
        
        return result
        
    # Méthode pour récupérer tous les événements dans la base de données
    def recuperer_ev(self):
        mydb, connection = self._get_db_connection()
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM evenement")
        results = mycursor.fetchall()
        mycursor.close()
    
        # Fermez la connexion à la base de données
        self._close_db_connection(mydb)
    
        return results

class Participant:
    
    """
    Cette classe Participant gère les opérations liées aux participants dans la base 
    de données, y compris l'ajout, la suppression, la modification, et la récupération 
    des participants. Elle effectue également des validations sur les entrées 
    telles que l'email, le numéro de téléphone et la date d'inscription
    """
    
    def __init__(self, nom_part, prenom_part, tel_part, email_part, date_inscription_part):
        self.nom_part = nom_part                                # Nom participant
        self.prenom_part = prenom_part                          # Prenom participant
        self.tel_part = tel_part                                # Telephone participant
        self.email_part = email_part                            # Email participant
        self.date_inscription_part = date_inscription_part      # Date d'inscription du participant

    # Méthode privée pour obtenir la connexion à la base de données
    def _get_db_connection(self):
        # Créez une instance de GestionBilletEvenementDB pour obtenir la connexion à la base de données
        db = GestionBilletEvenementDB(
            host="localhost",
            user="root",
            password="Stage2023",
            database="Reservation"
        )
        connection = db.get_connection()
        return db, connection
    
    # Méthode privée pour fermer la connexion à la base de données
    def _close_db_connection(self, db):
        db.close_connection()
    
    # Méthode pour ajouter un participant à la base de données
    def ajouter(self):
        
        if not self.valider_name(self.nom_part):
            raise ValueError("Le nom n'est pas valide")
            
        if not self.valider_name(self.prenom_part):
            raise ValueError("Le nom n'est pas valide")
        
        if not self._valider_telephone(self.tel_part):
            raise ValueError("Le numéro de téléphone n'est pas valide")
        
        if not self._valider_email(self.email_part):
            raise ValueError("L'email n'est pas valide")
        
        
        if not self._valider_date_inscription(self.date_inscription_part):
            raise ValueError("La date d'inscription n'est pas valide")
            
        mydb, connection = self._get_db_connection()
        
        query = "INSERT INTO participant (nom_part, prenom_part, tel_part, email_part, date_inscription_part) VALUES (%s, %s, %s, %s, %s)"
        values = (self.nom_part, self.prenom_part, self.tel_part, self.email_part, self.date_inscription_part)
        mycursor = connection.cursor()
        mycursor.execute(query, values)
        mycursor.close()

        # Fermez la connexion
        self._close_db_connection(mydb)
    
    # Méthode privée pour valider le format d'un email
    def _valider_email(self, email):
        # Utilisation d'une expression régulière pour valider l'email
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
    
    # Méthode privée pour valider le format d'un numéro de téléphone
    def _valider_telephone(self, telephone):
        # Utilisation d'une expression régulière pour valider le numéro de téléphone
        pattern = r'^\d{10}$'
        return re.match(pattern, telephone) is not None
    
    # Méthode privée pour valider la date d'inscription (doit être la date actuelle)
    def _valider_date_inscription(self, date_inscription):
        try:
            date = datetime.strptime(date_inscription, '%Y-%m-%d')
            return date.date() == datetime.now().date()
        except ValueError:
            return False
        
    def is_valider_name(self,name):
        # Le regex permet les lettres majuscules et minuscules, les espaces et les tirets, et doit avoir au moins un caractère.
        pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s\-]+$"
        return re.match(pattern, name) is not None
    
    # Méthode pour supprimer un participant de la base de données par son ID
    def supprimer(self, id_part):
        mydb, connection = self._get_db_connection()
        query = "DELETE FROM participant WHERE id_part = %s"
        value = (id_part,)
        mycursor = connection.cursor()
        mycursor.execute(query, value)
        mycursor.close()

        # Fermez la connexion
        self._close_db_connection(mydb)
    
    # Méthode pour modifier les détails d'un participant dans la base de données
    def modifier(self, nouveau_nom, nouveau_prenom, nouveau_tel, nouveau_email, nouvelle_date_inscription, id_part):
        if not self._valider_telephone(nouveau_tel):
            raise ValueError("Le numéro de téléphone n'est pas valide")
        
        if not self._valider_email(nouveau_email):
            raise ValueError("L'email n'est pas valide")
        
        if not self._valider_date_inscription(nouvelle_date_inscription):
            raise ValueError("La date d'inscription n'est pas valide")
            
        mydb, connection = self._get_db_connection()
        
        query = "UPDATE participant SET nom_part = %s, prenom_part = %s, tel_part = %s, email_part = %s, date_inscription_part = %s WHERE id_part = %s"
        values = (nouveau_nom, nouveau_prenom, nouveau_tel, nouveau_email, nouvelle_date_inscription, id_part)
        mycursor = connection.cursor()
        mycursor.execute(query, values)
        mycursor.close()
        
        # Fermez la connexion
        self._close_db_connection(mydb)

    # Méthode pour rechercher un participant par son ID
    def rechercher_par_id(self, id_participant):
        mydb, connection = self._get_db_connection()
        query = "SELECT email_part FROM participant WHERE id_part LIKE %s"
        value = (id_participant,)
        mycursor = connection.cursor()
        mycursor.execute(query, value)
        
        result = mycursor.fetchone()
        mycursor.close()
        
        # Fermez la connexion
        self._close_db_connection(mydb)
        
        return result
    
    # Méthode pour rechercher un participant par son email
    def rechercher_par_mail(self, mail):
        mydb, connection = self._get_db_connection()
        query = "SELECT * FROM participant WHERE email_part LIKE %s"
        value = (mail,)
        mycursor = connection.cursor()
        mycursor.execute(query, value)
        
        result = mycursor.fetchall()
        mycursor.close()
        
        # Fermez la connexion
        self._close_db_connection(mydb)
        
        return result
    
    # Méthode pour récupérer tous les participants dans la base de données
    def recuperer_part(self):
        mydb, connection = self._get_db_connection()
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM participant")
        
        results = mycursor.fetchall()
        mycursor.close()
        
        # Fermez la connexion
        self._close_db_connection(mydb)
        
        return results

class Billet:
    
    """
    Cette classe Billet gère les opérations liées aux billets dans la base de données, 
    y compris l'ajout, la suppression, la modification, la recherche par type et 
    la récupération de tous les billets. Elle utilise des méthodes privées pour gérer l
    a connexion à la base de données et effectue différentes opérations en fonction 
    des besoins.
    """
    
    def __init__(self, type_billet, prix_billet, id_ev, id_part):
        self.type_billet = type_billet   # Type billet
        self.prix_billet = prix_billet   # Prix billet
        self.id_ev = id_ev               # Identifiant evenement (Clé étrangère)   
        self.id_part = id_part           # Identifiant participant (Clé étrangère)

    # Méthode privée pour obtenir la connexion à la base de données
    def _get_db_connection(self):
        # Créez une instance de GestionBilletEvenementDB pour obtenir la connexion à la base de données
        db = GestionBilletEvenementDB(
            host="localhost",
            user="root",
            password="Stage2023",
            database="Reservation"
        )
        connection = db.get_connection()
        return db, connection
    
    # Méthode privée pour fermer la connexion à la base de données
    def _close_db_connection(self, db):
        db.close_connection()

    # Méthode pour ajouter un billet à la base de données
    def ajouter(self, id_ev):
        mydb, connection = self._get_db_connection()
        
        query = "INSERT INTO billet (type_billet, prix_billet, id_ev, id_part) VALUES (%s, %s, %s, %s)"
        values = (self.type_billet, self.prix_billet, id_ev, self.id_part)
        mycursor = connection.cursor()
        try:
            mycursor.execute(query, values)
        except mysql.connector.errors.DatabaseError.column as e:
            print(e)
        mycursor.close()

        # Fermez la connexion
        self._close_db_connection(mydb)

    # Méthode pour supprimer un billet de la base de données par son ID
    def supprimer(self, id_billet):
        mydb, connection = self._get_db_connection()
        
        query = "DELETE FROM billet WHERE id_billet = %s"
        value = (id_billet,)
        mycursor = connection.cursor()
        mycursor.execute(query, value)
        mycursor.close()
        
        # Fermez la connexion
        self._close_db_connection(mydb)

    # Méthode pour modifier les détails d'un billet dans la base de données
    def modifier(self, nouveau_type, nouveau_prix, nouveau_id_ev, nouveau_id_part, id_billet):
        mydb, connection = self._get_db_connection()
        
        query = "UPDATE billet SET type_billet = %s, prix_billet = %s, id_ev = %s, id_part = %s WHERE id_billet = %s"
        values = (nouveau_type, nouveau_prix, nouveau_id_ev, nouveau_id_part, id_billet)
        mycursor = connection.cursor()
        mycursor.execute(query, values)
        mycursor.close()

        # Fermez la connexion
        self._close_db_connection(mydb)
    
    # Méthode pour rechercher des billets par type (pattern de recherche)
    def rechercher_par_type(self, search_pattern):
        mydb, connection = self._get_db_connection()
        
        query = "SELECT * FROM billet WHERE type_billet LIKE %s"
        value = (search_pattern,)
        
        mycursor = connection.cursor()
        mycursor.execute(query, value)
        results = mycursor.fetchall()
        mycursor.close()
        
        return results
    
    # Méthode pour récupérer tous les billets dans la base de données
    def recuperer_billet(self):
        mydb, connection = self._get_db_connection()
        mycursor = connection.cursor()
        mycursor.execute("""
                         SELECT billet.id_billet,
                         billet.type_billet,
                         billet.prix_billet,
                         evenement.nom_ev,
                         participant.email_part
                         FROM billet, evenement, participant
                         WHERE billet.id_ev = evenement.id_ev and billet.id_part = participant.id_part
                         """)        
        results = mycursor.fetchall()
        mycursor.close()
        
        # Fermez la connexion
        self._close_db_connection(mydb)
        
        return results

class GestionBilletEvenementDB:
    
    """
    Cette classe GestionBilletEvenementDB gère la création de la base de données et 
    des tables associées si elles n'existent pas. Elle fournit également des méthodes 
    pour obtenir et fermer la connexion à la base de données. Elle est utilisée par 
    les autres classes pour interagir avec la base de données MySQL.
    """
    
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.create_database()

    # Méthode pour créer la base de données et les tables si elles n'existent pas
    def create_database(self):
        try:
            # Établir une connexion à la base de données du serveur MySQL
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            cursor = self.conn.cursor()

            # Créer la base de données si elle n'existe pas
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {self.database}')
            cursor.execute(f'USE {self.database}')

            # Créer la table Evenement
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Evenement (
                    id_ev INT AUTO_INCREMENT PRIMARY KEY,
                    nom_ev VARCHAR(45) NOT NULL UNIQUE,
                    date_ev DATE NOT NULL,
                    lieu_ev VARCHAR(45) NOT NULL,
                    description_ev VARCHAR(45) NOT NULL,
                    capacite_ev INT NOT NULL
                )
            ''')
            
            # Créer la table Participant
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Participant (
                    id_part INT AUTO_INCREMENT PRIMARY KEY,
                    nom_part VARCHAR(45) NOT NULL,
                    prenom_part VARCHAR(45) NOT NULL,
                    tel_part VARCHAR(15) NOT NULL UNIQUE,
                    email_part VARCHAR(60) NOT NULL UNIQUE,
                    date_inscription DATE NOT NULL
                )
            ''')

            # Créer la table Billet
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Billet (
                    id_billet INT AUTO_INCREMENT PRIMARY KEY,
                    type_billet VARCHAR(45) NOT NULL UNIQUE,
                    prix_billet DECIMAL(10, 0) NOT NULL,
                    id_ev INT,
                    id_part INT,
                    FOREIGN KEY (id_ev) REFERENCES Evenement(id_ev),
                    FOREIGN KEY (id_part) REFERENCES Participant(id_part)
                )
            ''')

            # Valider les modifications dans la base de données
            self.conn.commit()
            cursor.close()
        except mysql.connector.Error as e:
            print("Erreur lors de la création de la base de données:", e)

    # Méthode pour obtenir la connexion à la base de données
    def get_connection(self):
        return self.conn

    # Méthode pour fermer la connexion à la base de données
    def close_connection(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()


