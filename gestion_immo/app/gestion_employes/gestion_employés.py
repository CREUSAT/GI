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
