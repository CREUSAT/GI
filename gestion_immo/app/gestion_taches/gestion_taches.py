class GestionnaireTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self):
        # L'indentation est nécessaire pour le corps de la fonction
        index = int(input("Entrez l'index de la tâche à supprimer : "))
        del self.taches[index]

    def afficher_taches(self):
        print("Liste des tâches :")
        for i, tache in enumerate(self.taches):
            print(f"{i}. {tache}")
