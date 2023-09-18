#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ce fichier fait partie intégrante d'un projet de gestion de réservation de billets pour
des événements. Il englobe la définition de la classe "Application", dont la mission 
est d'élaborer une interface graphique tout en s'appuyant sur les classes du module 
"Classes". Ainsi, il vise à fournir une application complète pour la gestion de 
réservations d'événements et de billets.
"""


import tkinter as tk
from tkinter import ttk, messagebox
from Classes import Evenement,Participant,Billet


class Application(tk.Tk):
    def __init__(self):
        # Initialise la fenêtre principale de l'application
        tk.Tk.__init__(self)
        
        # Propriétés de la fenêtre
        self.menu_selected = None
        self.column_headings = (" ", " ", " ", " ", " ", " ", " ")
        self.columns = ("col1", "col2", "col3", "col4", "col5", "col6")
        self.col_widths = (200, 200, 200, 200, 200, 200)
        self.title("GESTION DE LA RÉSERVATION DES BILLETS")
        self.geometry("1400x900")
        self.minsize(1400, 700)
        
        # Crée l'interface graphique
        self.creer_interface()
    
    # Methode qui cree l'interface graphique
    def creer_interface(self):
        # Crée l'entête et le conteneur principal
        self.creer_entete()
        self.creer_conteneur_principal()

    # Methode qui cree l'entete de la fenetre
    def creer_entete(self):
        # Crée l'en-tête de l'application
        self.entete = tk.Frame(self, bg="orange", height=25)
        self.entete.pack(fill=tk.X)
    
        # Crée le titre
        self.creer_titre()
    
        # Crée le bloc du menu
        self.bloc_menu = tk.Frame(self.entete, bg="orange")
        self.bloc_menu.pack(side=tk.BOTTOM, pady=10)
    
        # Bouton "Événements"
        self.btn_produit = tk.Button(self.bloc_menu, text="Événements", command=self.show_evenements, font=("Arial", 19), width=10, bg="yellow")
        self.btn_produit.pack(side=tk.LEFT, padx=5)
    
        # Bouton "Billets"
        self.btn_categorie = tk.Button(self.bloc_menu, text="Billets", command=self.show_billets, font=("Arial", 19), width=10, bg="yellow")
        self.btn_categorie.pack(side=tk.LEFT, padx=5)
        
        # Bouton "Participants"
        self.btn_categorie = tk.Button(self.bloc_menu, text="Participants", command=self.show_participants, font=("Arial", 19), width=10, bg="yellow")
        self.btn_categorie.pack(side=tk.LEFT, padx=5)

    # Methode qui cree le titre principale de l'application
    def creer_titre(self):
        # Crée le titre de l'application
        self.titre = tk.Label(self.entete, text="GESTION DE LA RÉSERVATION DES BILLETS", font=("Arial", 35, "bold"), bg="orange", height=4)
        self.titre.pack(side=tk.LEFT, padx=0, pady=0, fill=tk.BOTH, expand=True)
      
        
    def creer_conteneur_principal(self):
        # Crée un conteneur principal pour l'application
        self.conteneur_principal = tk.Frame(self)
        self.conteneur_principal.pack(fill=tk.BOTH, expand=True)
    
        # Appelle la méthode pour créer le bloc de gauche et la table
        self.creer_bloc_gauche()
        self.create_table()
    
    def creer_bloc_gauche(self):
        # Crée un bloc gauche pour les boutons CRUD et la recherche
        self.bloc_gauche = tk.Frame(self.conteneur_principal, bg="black", width=230)
        self.bloc_gauche.pack(side=tk.LEFT, fill=tk.Y)
        self.bloc_gauche.pack_propagate(False)
    
        # Appelle la méthode pour créer les boutons CRUD et initialise les éléments de recherche
        self.creer_boutons_crud()
        self.label_search = None
        self.entry_search = None
        self.submit_search = None
    
    def creer_boutons_crud(self):
        # Crée les boutons CRUD (Ajouter, Modifier, Supprimer, Rechercher) et les configure
        self.btn_ajouter = tk.Button(self.bloc_gauche, text="Ajouter", command=self.add_selected, font=("Arial", 18), width=10, bg="yellow")
        self.btn_ajouter.pack(pady=20)
    
        self.btn_modifier = tk.Button(self.bloc_gauche, text="Modifier", command=self.modify_selected, font=("Arial", 18), width=10, bg="yellow")
        self.btn_modifier.pack(pady=20)
        
        self.btn_supprimer = tk.Button(self.bloc_gauche, text="Supprimer", command=self.delete_selected, font=("Arial", 18), width=10, bg="yellow")
        self.btn_supprimer.pack(pady=20)
        
        self.btn_rechercher = tk.Button(self.bloc_gauche, text="Rechercher", command=self.search, width=10, font=("Arial", 18), bg="yellow")
        self.btn_rechercher.pack(pady=20)
    
        
    # Methode qui cree la table et sa mise en forme    
    def create_table(self):
        # Assurez-vous que la table existe déjà
        if hasattr(self, "treeview"):
            self.treeview.destroy()
            self.treeview = None
        
        # Créez un cadre (frame) pour contenir la table
        self.table_frame = tk.Frame(self.conteneur_principal, background="orange")
        self.table_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=(0,))
        
        table_width = 1350
        table_height = 50
        
        # Créez un Treeview pour afficher les données sous forme de tableau
        self.treeview = ttk.Treeview(self.table_frame, show="headings")
        self.treeview.place(x=0, y=0, height=600)
        
        # Ajoutez une barre de défilement vertical à la table
        scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.treeview.yview)
        scrollbar.place(x=table_width, y=0, height=table_height)
        self.treeview.configure(yscroll=scrollbar.set)
        self.table_frame.configure(width=table_width, height=table_height)
        
        # Ajoutez les colonnes à la table
        self.treeview["columns"] = self.columns
        
        # Spécifiez les largeurs des colonnes et ajoutez les en-têtes de colonnes
        for i, col in enumerate(self.treeview["columns"]):
            self.treeview.column(col, width=self.col_widths[i], anchor="w")
            self.treeview.heading(col, text=self.column_headings[i], anchor='w')
        
        # Configurez le style de la table et des en-têtes de colonnes
        style = ttk.Style()
        style.configure("Treeview", background="", foreground="black", font=("Arial", 16))
        style.configure("Treeview.Heading", foreground="black", font=("Arial", 18))

    # Methode pour mettre à jour les colonnes de la table
    def update_table_columns(self, columns, col_widths):
        self.treeview["columns"] = columns 
        
        # Spécifiez les largeurs des colonnes et les en-têtes de colonnes
        for i, col in enumerate(self.treeview["columns"]):
            self.treeview.column(col, width=col_widths[i], anchor="w")
            self.treeview.heading(col, text=columns[i])
        
        # Mettez en majuscules les en-têtes de colonnes
        for column in columns:
            self.treeview.heading(column, text=column.capitalize())
        
        # Mettez à jour la table
        self.treeview.update()

     
    # Methode qui affiche la liste des evenements  
    def show_evenements(self):   # nb_search represente le nombre d'occurence trouvés lors d'une recherche
        # Vérifiez si un bouton de recherche est affiché et supprimez-le le cas échéant
        if self.label_search:
            self.remove_search_button()
        
        # Créez une instance de la classe Evenement pour interagir avec la table Evenement de la base de données
        evenement = Evenement(None, None, None, None, None)
        
        # Récupérez tous les événements de la base de données
        evenements = evenement.recuperer_ev()
        
        # Définissez les en-têtes de colonnes pour afficher les données dans le Treeview
        self.column_headings = ("Identifiant", "Nom", "Date", "Lieu", "Description", "Capacité")
        self.columns = ("col1", "col2", "col3", "col4", "col5", "col6")  
        self.col_widths = (140, 230, 140, 230, 250, 130)
        
        # Effacez le contenu actuel du tableau s'il existe
        self.clear_table()
        
        # Créez un nouveau tableau avec les en-têtes et les largeurs de colonnes définis précédemment
        self.create_table()
        
        # Parcourez la liste des événements récupérés de la base de données
        for evenement in evenements:
            # Insérez les données de l'événement dans le Treeview
            self.treeview.insert("", tk.END, values=(
                evenement[0],     # Identifiant de l'événement
                evenement[1],     # Nom de l'événement
                evenement[2],     # Date de l'événement
                evenement[3],     # Lieu de l'événement
                evenement[4],     # Description de l'événement
                evenement[5],     # Capacité de l'événement
            ))
        
        # Marquez le menu actuellement sélectionné comme "evenements"
        self.menu_selected = "evenements"
        
        # Affichez le nombre total d'événements dans un label
        nb_evenement = len(evenements)
        nb_evenement_label = tk.Label(self.table_frame, text=f"Nombre de produits : {nb_evenement} ", font=("Arial", 15, "bold"), bg="white", width=25, anchor="w")
        nb_evenement_label.place(x=0, y=605)

        
        
    # Methode qui permet d'afficher la liste des billets    
    def show_billets(self):   # nb_search represente le nombre d'occurence trouvés lors d'une recherche
        # Vérifiez si un bouton de recherche est affiché et supprimez-le le cas échéant
        if self.label_search:
            self.remove_search_button()
        
        # Créez une instance de la classe Billet pour interagir avec la table Billet de la base de données
        billet = Billet(None, None, None, None)
        
        # Récupérez tous les billets de la base de données
        billets = billet.recuperer_billet()
        
        # Définissez les en-têtes de colonnes pour afficher les données dans le Treeview
        self.column_headings = ("Identifiant", "Type de billet", "Prix du billet", "Événement", "Participant")
        self.columns = ("col1", "col2", "col3", "col4", "col5")  
        self.col_widths = (200, 230, 150, 280, 260)
    
        # Effacez le contenu actuel du tableau s'il existe
        self.clear_table()
        
        # Créez un nouveau tableau avec les en-têtes et les largeurs de colonnes définis précédemment
        self.create_table()
        
        # Parcourez la liste des billets récupérés de la base de données
        for billet in billets:
            # Créez une instance de la classe Evenement pour interagir avec la table Evenement de la base de données
            evenement = Evenement(None, None, None, None, None)
            
            # Obtenez l'ID de l'événement depuis le billet en cours
            id_evenement = billet[3]
            
            # Recherchez l'événement associé à cet ID
            nom_ev = evenement.rechercher_par_id(id_evenement)
    
            # Créez une instance de la classe Participant pour interagir avec la table Participant de la base de données
            participant = Participant(None, None, None, None, None)
            
            # Obtenez l'ID du participant depuis le billet en cours
            id_participant = billet[4]
            
            # Recherchez le participant associé à cet ID
            part = participant.rechercher_par_id(id_participant)
            
            # Obtenez le nom et le prénom du participant
            nom, prenom = part[0], part[1]
            
            # Insérez les données du billet dans le Treeview
            self.treeview.insert("", tk.END, values=(
                billet[0],         # Identifiant du billet
                billet[1],         # Type de billet
                billet[2],         # Prix du billet
                nom_ev,            # Nom de l'événement associé
                str(nom) + " " + str(prenom)  # Nom complet du participant associé
            ))
        
        # Marquez le menu actuellement sélectionné comme "billets"
        self.menu_selected = "billets"
        
        # Affichez le nombre total de billets dans un label
        nb_billet = len(billets)
        nb_billet_label = tk.Label(self.table_frame, text=f"Nombre de produits : {nb_billet} ", font=("Arial", 15, "bold"), bg="white", width=25, anchor="w")
        nb_billet_label.place(x=0, y=605)

        
    # Methode qui affiche la liste des evenements
    def show_participants(self):   # nb_search represente le nombre d'occurence trouvés lors d'une recherche
        # Vérifiez si un bouton de recherche est affiché et supprimez-le le cas échéant
        if self.label_search:
            self.remove_search_button()
        
        # Créez une instance de la classe Participant pour interagir avec la table Participant de la base de données
        participant = Participant(None, None, None, None, None)
        
        # Récupérez tous les participants de la base de données
        participants = participant.recuperer_part()
        
        # Définissez les en-têtes de colonnes pour afficher les données dans le Treeview
        self.column_headings = ("Identifiant", "Nom", "Prénom", "Téléphone", "Email", "Date d'inscription")
        self.columns = ("col1", "col2", "col3", "col4", "col5", "col6")  
        self.col_widths = (140, 230, 140, 210, 250, 150)
        
        # Effacez le contenu actuel du tableau s'il existe
        self.clear_table()
        
        # Créez un nouveau tableau avec les en-têtes et les largeurs de colonnes définis précédemment
        self.create_table()
        
        # Parcourez la liste des participants récupérés de la base de données
        for participant in participants:
            # Insérez les données du participant dans le Treeview
            self.treeview.insert("", tk.END, values=(
                participant[0],     # Identifiant du participant
                participant[1],     # Nom du participant
                participant[2],     # Prénom du participant
                participant[3],     # Téléphone du participant
                participant[4],     # Email du participant
                participant[5]      # Date d'inscription du participant
            ))
        
        # Marquez le menu actuellement sélectionné comme "participants"
        self.menu_selected = "participants"
        
        # Affichez le nombre total de participants dans un label
        nb_participant = len(participants)
        nb_participant_label = tk.Label(self.table_frame, text=f"Nombre de produits : {nb_participant} ", font=("Arial", 15, "bold"), bg="white", width=24, anchor="w")
        nb_participant_label.place(x=0, y=605)
    
    # Methode pour effacer la table
    def clear_table(self):
        # Vérifiez si le cadre de la table existe
        if hasattr(self, "table_frame"):
            # Détruisez le cadre de la table pour effacer son contenu
            self.table_frame.destroy()
            self.table_frame = None

    # Methode qui permet de creer un formulaire d'ajout en fonciton de la table selectionnée
    def add_selected(self):
        # Récupérez le nom de la table sélectionnée depuis le menu
        table_name = self.menu_selected
        
        # Vérifiez si un nom de table a été sélectionné
        if table_name:
            # Créez une fenêtre de formulaire pour ajouter des données en fonction de la table sélectionnée
            
            # Si la table sélectionnée est "evenements"
            if table_name == "evenements":
                # Créez une fenêtre de formulaire pour ajouter un événement
                form = tk.Toplevel(self)
                form.geometry("600x500")
                form.title("Ajouter un Événement")
                
                # Ajoutez des champs de saisie pour les informations de l'événement
                label_nom = tk.Label(form, text="Nom de l'événement:", bg="orange", fg="white", font=("Arial", 16), width=25)
                label_nom.pack(pady=10)
                entry_nom = tk.Entry(form, width=25)
                entry_nom.pack()
                
                label_date = tk.Label(form, text="Date de l'événement:", bg="orange", fg="white", font=("Arial", 16), width=25)
                label_date.pack(pady=10)
                entry_date = tk.Entry(form, width=25)
                entry_date.pack()
                
                label_lieu = tk.Label(form, text="Lieu de l'événement:", bg="orange", fg="white", font=("Arial", 16), width=25)
                label_lieu.pack(pady=10)
                entry_lieu = tk.Entry(form, width=25)
                entry_lieu.pack()
                
                label_desc = tk.Label(form, text="Description de l'événement:", bg="orange", fg="white", font=("Arial", 16), width=25)
                label_desc.pack(pady=10)
                entry_desc = tk.Entry(form, width=25)
                entry_desc.pack()
                
                label_capacite = tk.Label(form, text="Capacité de l'événement:", bg="orange", fg="white", font=("Arial", 16), width=25)
                label_capacite.pack(pady=10)
                entry_capacite = tk.Entry(form, width=25)
                entry_capacite.pack()
                
                # Ajoutez un bouton de soumission pour ajouter l'événement
                submit_button = tk.Button(form, text="Valider", command=lambda: self.handle_add_event(entry_nom, entry_date, entry_lieu, entry_desc, entry_capacite, form))
                submit_button.pack()
                
            # Si la table sélectionnée est "billets"
            elif table_name == "billets":
                # Créez une fenêtre de formulaire pour ajouter un billet
                form = tk.Toplevel(self)
                form.geometry("600x500")
                form.title("Ajouter un Billet")
                
                # Ajoutez des champs de saisie pour les informations du billet
                label_type = tk.Label(form, text="Type du billet:", bg="orange", fg="white", font=("Arial", 16), width=25)
                label_type.pack(pady=10)
                entry_type = tk.Entry(form, width=25)
                entry_type.pack()
                
                label_prix = tk.Label(form, text="Prix du billet:", bg="orange", fg="white", font=("Arial", 16), width=25)
                label_prix.pack(pady=10)
                entry_prix = tk.Entry(form, width=25)
                entry_prix.pack()
                
                label_ev = tk.Label(form, text="Événement associé:", bg="orange", fg="white", font=("Arial", 16), width=25)
                label_ev.pack(pady=10)
                
                # Créez une liste déroulante des événements existants
                evenement = Evenement(None, None, None, None, None)
                evenements = evenement.recuperer_ev()
                list_ev = []
                
                for ev in evenements:
                    list_ev.append(ev[1])
                
                ev_combobox = ttk.Combobox(form, values=list_ev, state="readonly", width=23)
                ev_combobox.pack()
                
                label_part = tk.Label(form, text="Participant associé:", bg="orange", fg="white", font=("Arial", 16), width=25)
                label_part.pack(pady=10)
                
                # Créez une liste déroulante des participants existants
                participant = Participant(None, None, None, None, None)
                participants = participant.recuperer_part()
                list_part = []
                
                for part in participants:
                    list_part.append(part[4])
                
                part_combobox = ttk.Combobox(form, values=list_part, state="readonly", width=23)
                part_combobox.pack()
                
                # Ajoutez un bouton de soumission pour ajouter le billet
                submit_button = tk.Button(form, text="Valider", command=lambda: self.handle_add_billet(entry_type, entry_prix, ev_combobox, part_combobox, form))
                submit_button.pack()
                
            # Si la table sélectionnée est "participants"
            elif table_name == "participants":
                # Créez une fenêtre de formulaire pour ajouter un participant
                form = tk.Toplevel(self)
                form.geometry("600x500")
                form.title("Ajouter un Participant")
                
                # Ajoutez des champs de saisie pour les informations du participant
                label_nom = tk.Label(form, text="Nom du participant:", bg="orange", fg="white", font=("Arial", 16), width=30)
                label_nom.pack(pady=10)
                entry_nom = tk.Entry(form, width=30)
                entry_nom.pack()
                
                label_prenom = tk.Label(form, text="Prénom du participant:", bg="orange", fg="white", font=("Arial", 16), width=30)
                label_prenom.pack(pady=10)
                entry_prenom = tk.Entry(form, width=30)
                entry_prenom.pack()
                
                label_tel = tk.Label(form, text="Téléphone du participant:", bg="orange", fg="white", font=("Arial", 16), width=30)
                label_tel.pack(pady=10)
                entry_tel = tk.Entry(form, width=30)
                entry_tel.pack()
                
                label_email = tk.Label(form, text="Email du participant:", bg="orange", fg="white", font=("Arial", 16), width=30)
                label_email.pack(pady=10)
                entry_email = tk.Entry(form, width=30)
                entry_email.pack()
                
                label_date = tk.Label(form, text="Date d'inscription du participant:", bg="orange", fg="white", font=("Arial", 16), width=30)
                label_date.pack(pady=10)
                entry_date = tk.Entry(form, width=30)
                entry_date.pack()
                
                # Ajoutez un bouton de soumission pour ajouter le participant
                submit_button = tk.Button(form, text="Valider", command=lambda: self.handle_add_part(entry_nom, entry_prenom, entry_tel, entry_email, entry_date, form))
                submit_button.pack()
                
            # Affichez un avertissement si aucune table n'a été sélectionnée
            else:
                messagebox.showwarning("Aucune sélection", "Veuillez sélectionner une ligne à supprimer.")
    
    def handle_add_event(self, entry_nom, entry_date, entry_lieu, entry_desc, entry_capacite, form):
        """
        Cette méthode ajoute un nouvel événement à la base de données en utilisant les
        données saisies dans le formulaire, puis affiche une confirmation et ferme 
        le formulaire.
        """
        
        # Récupérez les données saisies dans les champs de formulaire
        nom_ev = entry_nom.get()
        date_ev = entry_date.get()
        lieu_ev = entry_lieu.get()
        description_ev = entry_desc.get()
        capacite_ev = entry_capacite.get()
        
        # Créez une instance de la classe Evenement avec les données
        event = Evenement(nom_ev, date_ev, lieu_ev, description_ev, capacite_ev)
        
        # Ajoutez l'événement à la base de données
        event.ajouter()
        
        # Affichez une boîte de dialogue d'information pour indiquer que l'ajout a été effectué
        messagebox.showinfo("Ajout", "Ajout Effectué")
        
        # Fermez la fenêtre du formulaire
        form.destroy()
        
        # Affichez la liste mise à jour des événements
        self.show_evenements()
    
    def handle_add_billet(self, entry_type, entry_prix, ev_combobox, part_combobox, form):
        """
        Cette methode est une version de la methode 'handle_add_event' pour 
        la table Billet
        """
        # Récupérez les données saisies dans les champs de formulaire
        type_b = entry_type.get()
        prix_b = entry_prix.get()
        ev_b = ev_combobox.get()
        
        # Recherchez l'ID de l'événement associé par son nom
        evenement = Evenement(None, None, None, None, None)
        id_ev = evenement.rechercher_par_nom(ev_b)[0][0]
        
        # Récupérez le nom du participant sélectionné dans la liste déroulante
        part_b = part_combobox.get()
        
        # Recherchez l'ID du participant associé par son email
        participant = Participant(None, None, None, None, None)
        id_part = participant.rechercher_par_mail(part_b)[0][0]
        
        # Créez une instance de la classe Billet avec les données
        billet = Billet(type_b, prix_b, ev_b, id_part)
        
        # Ajoutez le billet à la base de données avec l'ID de l'événement associé
        billet.ajouter(id_ev)
        
        # Affichez une boîte de dialogue d'information pour indiquer que l'ajout a été effectué
        messagebox.showinfo("Ajout", "Ajout Effectué")
        
        # Fermez la fenêtre du formulaire
        form.destroy()
        
        # Affichez la liste mise à jour des billets
        self.show_billets()
    
    def handle_add_part(self, entry_nom, entry_prenom, entry_tel, entry_email, entry_date, form):
        
        """
        Cette methode est une version de la methode 'handle_add_event' pour 
        la table Participant
        """
        
        # Récupérez les données saisies dans les champs de formulaire
        nom_part = entry_nom.get()
        prenom_part = entry_prenom.get()
        tel_part = entry_tel.get()
        email_part = entry_email.get()
        date_part = entry_date.get()
        
        # Créez une instance de la classe Participant avec les données
        part = Participant(nom_part, prenom_part, tel_part, email_part, date_part)
        
        # Ajoutez le participant à la base de données
        part.ajouter()
        
        # Affichez une boîte de dialogue d'information pour indiquer que l'ajout a été effectué
        messagebox.showinfo("Ajout", "Ajout Effectué")
        
        # Fermez la fenêtre du formulaire
        form.destroy()
        
        # Affichez la liste mise à jour des participants
        self.show_participants()

    # Méthode qui permet de modifier l'element selectionné d'une table    
    def modify_selected(self):
        # Récupère le nom de la table actuellement sélectionnée
        table_name = self.menu_selected
        # Récupère l'élément sélectionné dans le Treeview
        selected_item = self.treeview.selection()
        
        # Vérifie si un élément est sélectionné
        if selected_item:
            # Crée une fenêtre de formulaire pour la modification
            form = tk.Toplevel(self)
            form.geometry("600x400")
            
            # Selon la table sélectionnée, configure le titre du formulaire et récupère les valeurs de l'élément sélectionné
            if table_name == "evenements":
                form.title("Modifier un événement")
                item_values = self.treeview.item(selected_item)["values"]
    
                # Crée des étiquettes et des champs de saisie pour chaque attribut de l'événement avec pré-remplissage des valeurs actuelles
                label_nom = tk.Label(form, text="Nom de l'événement:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_nom.pack(pady=10)
                entry_nom = tk.Entry(form,width=25)
                entry_nom.pack()
                entry_nom.insert(tk.END, item_values[1])  # PrÃ©-remplit avec la valeur actuelle
    
                label_date = tk.Label(form, text="Date de l'événement:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_date.pack(pady=10)
                entry_date = tk.Entry(form,width=25)
                entry_date.pack()
                entry_date.insert(tk.END, item_values[2])  # PrÃ©-remplit avec la valeur actuelle
    
                label_lieu = tk.Label(form, text="Lieu de l'événement:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_lieu.pack(pady=10)
                entry_lieu = tk.Entry(form,width=25)
                entry_lieu.pack()
                entry_lieu.insert(tk.END, item_values[3])  # PrÃ©-remplit avec la valeur actuelle
    
                label_desc = tk.Label(form, text="Description de l'événement:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_desc.pack(pady=10)
                entry_desc = tk.Entry(form,width=25)
                entry_desc.pack()
                entry_desc.insert(tk.END, item_values[4])  # PrÃ©-remplit avec la valeur actuelle
    
                label_capacite = tk.Label(form, text="CapacitÃ© de l'événement:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_capacite.pack(pady=10)
                entry_capacite = tk.Entry(form,width=25)
                entry_capacite.pack()
                entry_capacite.insert(tk.END, item_values[5])  # PrÃ©-remplit avec la valeur actuelle
    
                # Définit une fonction pour traiter la modification de l'événement
                def handle_modify_event():
                    nouveau_nom = entry_nom.get()
                    nouvelle_date = entry_date.get()
                    nouveau_lieu = entry_lieu.get()
                    nouvelle_description = entry_desc.get()
                    nouvelle_capacite = entry_capacite.get()
    
                    evenement = Evenement(None, None, None, None, None)
                    evenement.modifier(nouveau_nom, nouvelle_date, nouveau_lieu, nouvelle_description, nouvelle_capacite, item_values[0])
                    messagebox.showinfo("Modification", "Modification effectuée")
                    self.show_evenements()
                    form.destroy()
    
                # Crée un bouton pour valider la modification
                submit_button = tk.Button(form, text="Valider", command=handle_modify_event)
                submit_button.pack()
    
            elif table_name == "billets":
                # (Code similaire pour la modification des billets)

                form.title("Modifier un billet")
                item_values = self.treeview.item(selected_item)["values"]
    
                label_type = tk.Label(form, text="Type du billet:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_type.pack(pady=10)
                entry_type = tk.Entry(form, width=25)
                entry_type.pack()
                entry_type.insert(tk.END, item_values[1])  # PrÃ©-remplit avec la valeur actuelle
    
                label_prix = tk.Label(form, text="Prix du billet:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_prix.pack(pady=10)
                entry_prix = tk.Entry(form, width=25)
                entry_prix.pack()
                entry_prix.insert(tk.END, item_values[2])  # PrÃ©-remplit avec la valeur actuelle
    
                label_ev = tk.Label(form, text="Evenement associé:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_ev.pack(pady=10)
                entry_ev = tk.Entry(form, width=25)
                entry_ev.pack()
                entry_ev.insert(tk.END, item_values[3])  # PrÃ©-remplit avec la valeur actuelle
    
                label_part = tk.Label(form, text="Participant associé:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_part.pack(pady=10)
                entry_part = tk.Entry(form, width=25)
                entry_part.pack()
                entry_part.insert(tk.END, item_values[4])  # PrÃ©-remplit avec la valeur actuelle
    
                
                def handle_modify_billet():
                    type_b= entry_type.get()
                    prix_b = entry_prix.get()
                    ev_b = entry_ev.get()
                    part_b = entry_part.get()
                    
                    billet = Billet(None, None, None, None)
                    print(item_values[0])
                    billet.modifier(type_b,prix_b,ev_b,part_b,item_values[0])
                    messagebox.showinfo("Modification", "Modification effectuée")
                    self.show_billets()
                    form.destroy()
    
                submit_button = tk.Button(form, text="Valider", command=handle_modify_billet)
                submit_button.pack()
                
            elif table_name == "participants":
                # (Code similaire pour la modification des participants)
                form.title("Modifier un participant")
                item_values = self.treeview.item(selected_item)["values"]
    
                label_nom = tk.Label(form, text="Nom du partcipant:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_nom.pack(pady=10)
                entry_nom = tk.Entry(form, width=25)
                entry_nom.pack()
                entry_nom.insert(tk.END, item_values[1])  # PrÃ©-remplit avec la valeur actuelle
    
                label_prenom = tk.Label(form, text="Prénom du partcipant:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_prenom.pack(pady=10)
                entry_prenom = tk.Entry(form, width=25)
                entry_prenom.pack()
                entry_prenom.insert(tk.END, item_values[2])  # PrÃ©-remplit avec la valeur actuelle
    
                label_tel = tk.Label(form, text="Téléphone du partcipant:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_tel.pack(pady=10)
                entry_tel = tk.Entry(form, width=25)
                entry_tel.pack()
                if len(str(item_values[3])) != 10:
                    item_values[3] = str(0) + str(item_values[3])
                print(item_values[3])
                entry_tel.insert(tk.END, item_values[3])  # PrÃ©-remplit avec la valeur actuelle
    
                label_email = tk.Label(form, text="Email du partcipant:", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_email.pack(pady=10)
                entry_email = tk.Entry(form, width=25)
                entry_email.pack()
                entry_email.insert(tk.END, item_values[4])  # PrÃ©-remplit avec la valeur actuelle
    
                label_date = tk.Label(form, text="Date d'inscription du participant':", bg="orange", fg="white", font=("Arial", 16),width=25)
                label_date.pack(pady=10)
                entry_date = tk.Entry(form, width=25)
                entry_date.pack()
                entry_date.insert(tk.END, item_values[5])  # PrÃ©-remplit avec la valeur actuelle
    
                def handle_modify_part():
                    nom = entry_nom.get()
                    prenom = entry_prenom.get()
                    tel = entry_tel.get()
                    email = entry_email.get()
                    date = entry_date.get()
    
                    part = Participant(None, None, None, None, None)
                    print(item_values[0])
                    part.modifier(nom,prenom,tel,email,date,item_values[0])
                    messagebox.showinfo("Modification", "Modification effectuée")
                    self.show_participants()
                    form.destroy()
    
                submit_button = tk.Button(form, text="Valider", command=handle_modify_part)
                submit_button.pack()

        else:
            # Affiche un avertissement si aucun élément n'est sélectionné pour la modification
            messagebox.showwarning("Aucune sélection", "Veuillez sélectionner une ligne à modifier.")

     
    # Methode qui permet de supprimer l'element selectionnée d'une table   
    def delete_selected(self):
        # Récupère l'élément sélectionné dans le Treeview
        selected_item = self.treeview.selection()
        
        # Vérifie si un élément est sélectionné
        if selected_item:
            # Récupère les valeurs de l'élément sélectionné
            values = self.treeview.item(selected_item)["values"]
            # Récupère le nom de la table actuellement sélectionnée
            table_name = self.menu_selected
        
            # Demande une confirmation à l'utilisateur avant la suppression
            confirmation = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer cet élément ?")
        
            if confirmation:
                # Supprime l'élément de la table correspondante
                if table_name == "evenements":
                    event = Evenement(values[1], values[2], values[3], values[4], values[5])
                    event.supprimer(values[0])  # Supprime l'événement en utilisant son identifiant
                elif table_name == "billets":
                    billet = Billet(values[1], values[2], values[3], values[4])
                    billet.supprimer(values[0])  # Supprime le billet en utilisant son identifiant
                elif table_name == "participants":
                    part = Participant(values[1], values[2], values[3], values[4], values[5])
                    part.supprimer(values[0])  # Supprime le participant en utilisant son identifiant
        
                # Supprime la ligne de la table
                self.treeview.delete(selected_item)
        else:
            # Affiche un avertissement si aucun élément n'est sélectionné pour la suppression
            messagebox.showwarning("Aucune sélection", "Veuillez sélectionner une ligne à supprimer.")
    
    def search(self):
        # Sélection de la table à partir du menu
        table_name = self.menu_selected
        if table_name:
            
            # Supprime les éléments de recherche précédents s'ils existent
            if self.label_search:
                self.remove_search_button()
            
            # En fonction de la table sélectionnée, configure les éléments d'interface utilisateur pour la recherche
            if table_name == "evenements":
                
                # Étiquette et champ de recherche pour les événements
                self.label_search = tk.Label(self.bloc_gauche, text="Nom de l'événement:", bg="orange", fg="white", font=("Arial", 16), width=18)
                self.label_search.pack()
                self.entry_search = tk.Entry(self.bloc_gauche)
                self.entry_search.pack()
                self.submit_search = tk.Button(self.bloc_gauche, text="Valider", command=lambda: self.filtrer_event())
                self.submit_search.pack()
      
            elif table_name == "billets":
                
                # Étiquette et champ de recherche pour les billets
                self.label_search = tk.Label(self.bloc_gauche, text="Type du billet:", bg="orange", fg="white", font=("Arial", 16), width=18)
                self.label_search.pack()
                self.entry_search = tk.Entry(self.bloc_gauche)
                self.entry_search.pack()
                self.submit_search = tk.Button(self.bloc_gauche, text="Valider", command=lambda: self.filtrer_billet())
                self.submit_search.pack()    
            
            elif table_name == "participants":
                
                 # Étiquette et champ de recherche pour les participants
                 self.label_search = tk.Label(self.bloc_gauche, text="Email du participant:", bg="orange", fg="white", font=("Arial", 16), width=18)
                 self.label_search.pack()
                 self.entry_search = tk.Entry(self.bloc_gauche)
                 self.entry_search.pack()
                 self.submit_search = tk.Button(self.bloc_gauche, text="Valider", command=lambda: self.filtrer_part())
                 self.submit_search.pack()  
          
        else:
            messagebox.showwarning("Aucune sélection", "Veuillez sélectionner une table.")
    
    def filtrer_event(self):
        # Récupère la valeur de recherche
        search_value = self.entry_search.get()
        # Crée un motif de recherche avec le caractère '%' pour rechercher des correspondances partielles
        nom = f"%{search_value}%"
        
        evenement = Evenement(None, None, None, None, None)
        results = evenement.rechercher_par_nom(nom)
        
        # Efface les données actuelles dans la table
        self.treeview.delete(*self.treeview.get_children())
    
        # Remplit la table avec les résultats de la recherche
        for result in results:
            self.treeview.insert("", tk.END, values=(result[0], result[1], result[2], result[3], result[4], result[5]))
    
        # Supprime les éléments d'interface utilisateur de recherche
        self.remove_search_button()
        
        # Affiche le nombre de résultats de la recherche
        nb_search = len(results)
        nb_search_label = tk.Label(self.table_frame, text=f"Nombre de produits : {nb_search} ", font=("Arial", 15, "bold"), bg="white", width=24, anchor="w")
        nb_search_label.place(x=0, y=605)
    
    # Les fonctions filtrer_billet et filtrer_part sont similaires, mais adaptées à leurs tables respectives
    def filtrer_billet(self):
        search_value = self.entry_search.get()
        search_pattern = f"%{search_value}%"
        billet = Billet(None, None, None, None)
        results = billet.rechercher_par_type(search_pattern)
        
        self.treeview.delete(*self.treeview.get_children())

        for result in results:
            self.treeview.insert("", tk.END, values=(result[0], result[1], result[2], result[3], result[4]))

        self.remove_search_button()
        
        nb_search = len(results)
        nb_search_label = tk.Label(self.table_frame, text=f"Nombre de produits : {nb_search} ", font=("Arial", 15, "bold"), bg="white", width=24, anchor="w")
        nb_search_label.place(x=0, y=605)

    def filtrer_part(self):
        search_value = self.entry_search.get()        
        part = Participant(None, None, None, None, None)
        results = part.rechercher_par_mail(search_value)
        
        self.treeview.delete(*self.treeview.get_children())

        for result in results:
            self.treeview.insert("", tk.END, values=(result[0], result[1], result[2], result[3], result[4], result[5]))

        self.remove_search_button()
        
        nb_search = len(results)
        nb_search_label = tk.Label(self.table_frame, text=f"Nombre de produits : {nb_search} ", font=("Arial", 15, "bold"), bg="white", width=24, anchor="w")
        nb_search_label.place(x=0, y=605)

    
    
    def remove_search_button(self):
        # Supprime les éléments d'interface utilisateur de recherche
        self.entry_search.destroy()
        self.label_search.destroy()
        self.submit_search.destroy()
        self.label_search = None
        self.entry_search = None
        self.submit_search = None

app = Application()


# Fermeture de la connexion à la base de données
app.mainloop()


