class Categorie:
    """
    Représente une catégorie de produits dans PyInventory.
    """

    def __init__(self, nom, description):
        """
        Initialise une catégorie.

        :param nom: nom de la catégorie
        :param description: description de la catégorie
        """
        self.nom = nom
        self.description = description
        self.produits = []

    def ajouter_produit(self, produit):
        """
        Ajoute un produit à la catégorie.
        """
        self.produits.append(produit)

    def retirer_produit(self, reference):
        """
        Retire un produit de la catégorie à partir de sa référence.
        """
        for produit in self.produits:
            if produit.reference == reference:
                self.produits.remove(produit)
                return True
        return False

    def lister_produits(self):
        """
        Affiche tous les produits de la catégorie.
        """
        print(f"Catégorie: {self.nom} ({self.nb_produits()} produits)")
        for produit in self.produits:
            print(
                f"- {produit.reference}: {produit.nom} - "
                f"{produit.prix_ht:.2f}€ - Stock: {produit.stock}"
            )

    def nb_produits(self):
        """
        Retourne le nombre de produits dans la catégorie.
        """
        return len(self.produits)

    def valeur_totale(self):
        """
        Retourne la valeur totale du stock de la catégorie.
        """
        total = 0
        for produit in self.produits:
            total += produit.valeur_stock()
        return total
