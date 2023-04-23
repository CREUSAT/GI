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
