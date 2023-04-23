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
