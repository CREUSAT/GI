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
