class RapportsFinanciers:
    def __init__(self):
        self.depenses = []

    def ajouter_depense(self, depense):
        self.depenses.append(depense)

    def generer_rapport_depenses(self):
        # Le corps de la fonction doit être indenté
        total_depenses = sum(self.depenses)
        nombre_depenses = len(self.depenses)
        moyenne_depenses = total_depenses / nombre_depenses
        print(f"Total des dépenses : {total_depenses}")
        print(f"Nombre de dépenses : {nombre_depenses}")
        print(f"Moyenne des dépenses : {moyenne_depenses}")

    def generer_rapport_revenus(self):
        # Le corps de la fonction doit également être indenté
        pass
