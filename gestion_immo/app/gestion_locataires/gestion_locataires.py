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
