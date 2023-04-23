import tkinter as tk
from tkinter import ttk
import sqlite3

# Connectez-vous à la base de données SQLite (créez-la si elle n'existe pas)
conn = sqlite3.connect('gestion_immobiliere.db')
cursor = conn.cursor()

# Créez une table 'propriete' si elle n'existe pas
cursor.execute('''CREATE TABLE IF NOT EXISTS propriete
                  (id INTEGER PRIMARY KEY, adresse TEXT, type_propriete TEXT, statut TEXT, prix REAL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS tache
                  (id INTEGER PRIMARY KEY, description TEXT, date_limite TEXT, priorite INTEGER)''')

# Créez une table 'locataire' si elle n'existe pas
cursor.execute('''CREATE TABLE IF NOT EXISTS locataire
                  (id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, email TEXT, telephone TEXT, date_naissance TEXT)''')

# Créez une table 'paiement' si elle n'existe pas
cursor.execute('''CREATE TABLE IF NOT EXISTS paiement
                  (id INTEGER PRIMARY KEY, locataire_id INTEGER, montant REAL, date_paiement TEXT, methode_paiement TEXT, reference TEXT)''')

# Créez une table 'employe' si elle n'existe pas
cursor.execute('''CREATE TABLE IF NOT EXISTS employe
                  (id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, email TEXT, telephone TEXT, poste TEXT, salaire REAL)''')

# Créez une table 'document' si elle n'existe pas
cursor.execute('''CREATE TABLE IF NOT EXISTS document
                  (id INTEGER PRIMARY KEY, titre TEXT, date_creation TEXT, type_document TEXT, contenu TEXT)''')

# Créez une table 'contact' si elle n'existe pas
cursor.execute('''CREATE TABLE IF NOT EXISTS contact
                  (id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, email TEXT, telephone TEXT, relation TEXT)''')

# Créez une table 'analyse_rentabilite' si elle n'existe pas
cursor.execute('''CREATE TABLE IF NOT EXISTS analyse_rentabilite
                  (id INTEGER PRIMARY KEY, propriete_id INTEGER, total_revenus REAL, total_depenses REAL, profit REAL, taux_rentabilite REAL)''')

# Créez une table 'comptabilite' si elle n'existe pas
cursor.execute('''CREATE TABLE IF NOT EXISTS comptabilite
                  (id INTEGER PRIMARY KEY, categorie TEXT, montant REAL, date_operation TEXT, description TEXT)''')

# Validez les modifications et fermez la connexion
conn.commit()
conn.close()




# Module: Gestion des propriétés
# Module: Gestion des propriétés
class Propriete:
    def __init__(self, id, adresse, type_propriete, statut, prix):
        self.id = id
        self.adresse = adresse
        self.type_propriete = type_propriete
        self.statut = statut
        self.prix = prix

    def ajouter_propriete(self):
        pass  # Code pour ajouter une propriété à la base de données

    def supprimer_propriete(self):
        pass  # Code pour supprimer une propriété de la base de données

    def modifier_propriete(self):
        pass  # Code pour modifier les détails d'une propriété dans la base de données

    def rechercher_propriete(self, filtre):
        pass  # Code pour rechercher des propriétés dans la base de données en fonction des critères de filtre

# Module: Gestion des taches
class GestionnaireTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self):
        index = int(input("Entrez l'index de la tâche à supprimer : "))
        del self.taches[index]

    def afficher_taches(self):
        print("Liste des tâches :")
        for i, tache in enumerate(self.taches):
            print(f"{i}. {tache}")


# Module: Gestion des Payments 
class GestionPaiements:
    def __init__(self):
        self.paiements = []

    def ajouter_paiement(self, paiement):
        self.paiements.append(paiement)

    def supprimer_paiement(self):
        # Le corps de la fonction doit être indenté
        index = int(input("Entrez l'index du paiement à supprimer : "))
        del self.paiements[index]

    def afficher_paiements(self):
        # Le corps de la fonction doit également être indenté
        for paiement in self.paiements:
            print(paiement)

    def chercher_paiement(self, reference):
        # Le corps de la fonction doit également être indenté
        for paiement in self.paiements:
            if paiement['reference'] == reference:
                return paiement
        return None

# Module: Gestion des Locataires
class GestionLocataires:
    def __init__(self):
        self.locataires = []

    def ajouter_locataire(self, locataire):
        self.locataires.append(locataire)

    def supprimer_locataire(self):
        # Le corps de la fonction doit être indenté
        index = int(input("Entrez l'index du locataire à supprimer : "))
        del self.locataires[index]

    def afficher_locataires(self):
        # Le corps de la fonction doit également être indenté
        for locataire in self.locataires:
            print(locataire)

    def chercher_locataire(self, nom):
        # Le corps de la fonction doit également être indenté
        for locataire in self.locataires:
            if locataire['nom'] == nom:
                return locataire
        return None

# Module: Gestion des Employees
class GestionEmployes:
    def __init__(self):
        self.employes = []

    def ajouter_employe(self, employe):
        self.employes.append(employe)

    def supprimer_employe(self):
        # Le corps de la fonction doit être indenté
        index = int(input("Entrez l'index de l'employé à supprimer : "))
        del self.employes[index]

    def afficher_employes(self):
        # Le corps de la fonction doit également être indenté
        for employe in self.employes:
            print(employe)

    def chercher_employe(self, nom):
        # Le corps de la fonction doit également être indenté
        for employe in self.employes:
            if employe['nom'] == nom:
                return employe
        return None

# Module: Gestion des Documents
class GestionDocuments:
    def __init__(self):
        self.documents = []

    def ajouter_document(self, document):
        self.documents.append(document)

    def supprimer_document(self):
        # Le corps de la fonction doit être indenté
        index = int(input("Entrez l'index du document à supprimer : "))
        del self.documents[index]

    def afficher_documents(self):
        # Le corps de la fonction doit également être indenté
        for document in self.documents:
            print(document)

    def chercher_document(self, titre):
        # Le corps de la fonction doit également être indenté
        for document in self.documents:
            if document['titre'] == titre:
                return document
        return None

# Module: Gestion des contacts
class GestionContacts:
    def __init__(self):
        self.contacts = []

    def ajouter_contact(self, contact):
        self.contacts.append(contact)

    def supprimer_contact(self):
        # Le corps de la fonction doit être indenté
        index = int(input("Entrez l'index du contact à supprimer : "))
        del self.contacts[index]

    def afficher_contacts(self):
        # Le corps de la fonction doit également être indenté
        for contact in self.contacts:
            print(contact)

    def chercher_contact(self, nom):
        # Le corps de la fonction doit également être indenté
        for contact in self.contacts:
            if contact['nom'] == nom:
                return contact
        return None

# Module: Comptabilite
class Comptable:
    def __init__(self):
        self.transactions = []

    def ajouter_transaction(self, transaction):
        self.transactions.append(transaction)

    def supprimer_transaction(self):
        # Le corps de la fonction doit être indenté
        index = int(input("Entrez l'index de la transaction à supprimer : "))
        del self.transactions[index]

    def afficher_transactions(self):
        # Le corps de la fonction doit également être indenté
        for transaction in self.transactions:
            print(transaction)

    def calculer_solde(self):
        # Le corps de la fonction doit également être indenté
        solde = sum(self.transactions)
        return solde

# Module: Analyse de Rentabilité
class AnalyseRentabilite:
    def __init__(self):
        self.depenses = []
        self.revenus = []

    def ajouter_depense(self, depense):
        self.depenses.append(depense)

    def ajouter_revenu(self, revenu):
        self.revenus.append(revenu)

    def calculer_depenses(self):
        # Le corps de la fonction doit être indenté
        total_depenses = sum(self.depenses)
        return total_depenses

    def calculer_revenus(self):
        # Le corps de la fonction doit également être indenté
        total_revenus = sum(self.revenus)
        return total_revenus

    def calculer_profit(self):
        # Le corps de la fonction doit également être indenté
        total_profit = self.calculer_revenus() - self.calculer_depenses()
        return total_profit
    



# Application principale avec interface utilisateur Tkinter
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion Immobilière")
        self.geometry("800x600")

        # Créez un notebook pour organiser les onglets de fonctionnalités
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")

        # Ajoutez des onglets pour chaque fonctionnalité
        propriete_tab = ttk.Frame(notebook)
        notebook.add(propriete_tab, text="Gestion des propriétés")

        locataire_tab = ttk.Frame(notebook)
        notebook.add(locataire_tab, text="Gestion des locataires")

        paiement_tab = ttk.Frame(notebook)
        notebook.add(paiement_tab, text="Gestion des paiements")

        rapport_financier_tab = ttk.Frame(notebook)
        notebook.add(rapport_financier_tab, text="Rapports financiers")

        employe_tab = ttk.Frame(notebook)
        notebook.add(employe_tab, text="Gestion des employés")

        document_tab = ttk.Frame(notebook)
        notebook.add(document_tab, text="Gestion des documents")

        contact_tab = ttk.Frame(notebook)
        notebook.add(contact_tab, text="Gestion des contacts")

        rentabilite_tab = ttk.Frame(notebook)
        notebook.add(rentabilite_tab, text="Analyse de rentabilité")

        comptabilite_tab = ttk.Frame(notebook)
        notebook.add(comptabilite_tab, text="Comptabilité")

        # Ajoutez des widgets (boutons, tableaux, etc.) pour chaque fonctionnalité
        # Gestion des propriétés
        ajouter_propriete_btn = ttk.Button(propriete_tab, text="Ajouter une propriété", command=self.ajouter_propriete)
        ajouter_propriete_btn.pack()
        modifier_propriete_btn = ttk.Button(propriete_tab, text="Modifier une propriété", command=self.modifier_propriete)
        modifier_propriete_btn.pack()
        supprimer_propriete_btn = ttk.Button(propriete_tab, text="Supprimer une propriété", command=self.supprimer_propriete)
        supprimer_propriete_btn.pack()

        # Gestion des locataires
        ajouter_locataire_btn = ttk.Button(locataire_tab, text="Ajouter un locataire", command=self.ajouter_locataire)
        ajouter_locataire_btn.pack()
        modifier_locataire_btn = ttk.Button(locataire_tab, text="Modifier un locataire", command=self.modifier_locataire)
        modifier_locataire_btn.pack()
        supprimer_locataire_btn = ttk.Button(locataire_tab, text="Supprimer un locataire", command=self.supprimer_locataire)
        supprimer_locataire_btn.pack()

        # Gestion des paiements
        ajouter_paiement_btn = ttk.Button(paiement_tab, text="Ajouter un paiement", command=self.ajouter_paiement)
        ajouter_paiement_btn.pack()
        modifier_paiement_btn = ttk.Button(paiement_tab, text="Modifier un paiement", command=self.modifier_paiement)
        modifier_paiement_btn.pack()
        supprimer_paiement_btn = ttk.Button(paiement_tab, text="Supprimer un paiement", command=self.supprimer_paiement)
        supprimer_paiement_btn.pack()
        
        # Gestion des employés
        ajouter_employe_btn = ttk.Button(employe_tab, text="Ajouter un employé", command=self.ajouter_employe)
        ajouter_employe_btn.pack()
        modifier_employe_btn = ttk.Button(employe_tab, text="Modifier un employé", command=self.modifier_employe)
        modifier_employe_btn.pack()
        supprimer_employe_btn = ttk.Button(employe_tab, text="Supprimer un employé", command=self.supprimer_employe)
        supprimer_employe_btn.pack()

        # Gestion des documents
        ajouter_document_btn = ttk.Button(document_tab, text="Ajouter un document", command=self.ajouter_document)
        ajouter_document_btn.pack()
        modifier_document_btn = ttk.Button(document_tab, text="Modifier un document", command=self.modifier_document)
        modifier_document_btn.pack()
        supprimer_document_btn = ttk.Button(document_tab, text="Supprimer un document", command=self.supprimer_document)
        supprimer_document_btn.pack()

        # Gestion des contacts
        ajouter_contact_btn = ttk.Button(contact_tab, text="Ajouter un contact", command=self.ajouter_contact)
        ajouter_contact_btn.pack()
        modifier_contact_btn = ttk.Button(contact_tab, text="Modifier un contact", command=self.modifier_contact)
        modifier_contact_btn.pack()
        supprimer_contact_btn = ttk.Button(contact_tab, text="Supprimer un contact", command=self.supprimer_contact)
        supprimer_contact_btn.pack()

        # Analyse de rentabilité
        calculer_rentabilite_btn = ttk.Button(rentabilite_tab, text="Calculer la rentabilité", command=self.calculer_rentabilite)
        calculer_rentabilite_btn.pack()

        # Comptabilité
        ajouter_operation_btn = ttk.Button(comptabilite_tab, text="Ajouter une opération", command=self.ajouter_operation)
        ajouter_operation_btn.pack()
        modifier_operation_btn = ttk.Button(comptabilite_tab, text="Modifier une opération", command=self.modifier_operation)
        modifier_operation_btn.pack()
        supprimer_operation_btn = ttk.Button(comptabilite_tab, text="Supprimer une opération", command=self.supprimer_operation)
        supprimer_operation_btn.pack()
