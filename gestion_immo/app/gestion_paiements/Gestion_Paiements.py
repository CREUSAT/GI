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
