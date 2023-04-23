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
