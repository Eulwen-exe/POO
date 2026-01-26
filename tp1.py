class Produit:
    """
    Représente un produit dans le système PyInventory.

    Cette classe permet de gérer les informations de base d’un produit
    (référence, nom, prix, stock) ainsi que des opérations courantes
    comme le calcul du prix TTC, la gestion du stock et la valeur totale.
    """

    # attributs de classe
    tva = 20
    """Taux de TVA appliqué aux produits (en pourcentage)."""

    nb_produits = 0
    """Compteur du nombre total d'instances de produits créées."""

    def __init__(self, reference, nom, prix_ht, stock):
        """
        Initialise un nouveau produit.

        :param reference: Code unique du produit
        :param nom: Nom du produit
        :param prix_ht: Prix hors taxes du produit
        :param stock: Quantité disponible en stock
        """
        self.reference = reference
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock

        Produit.nb_produits += 1

    def prix_ttc(self):
        """
        Calcule et retourne le prix TTC du produit.

        :return: Prix toutes taxes comprises
        """
        return self.prix_ht * (1 + Produit.tva / 100)

    def afficher(self):
        """
        Affiche les informations complètes du produit :
        référence, nom, prix HT, prix TTC et stock disponible.
        """
        print(
            f"Réf: {self.reference} | "
            f"{self.nom} | "
            f"{self.prix_ht:.2f}€ HT ({self.prix_ttc():.2f}€ TTC) | "
            f"Stock: {self.stock}"
        )

    def est_disponible(self):
        """
        Indique si le produit est disponible en stock.

        :return: True si le stock est supérieur à 0, False sinon
        """
        return self.stock > 0

    def ajouter_stock(self, quantite):
        """
        Ajoute une quantité donnée au stock du produit.

        :param quantite: Quantité à ajouter (doit être positive)
        """
        if quantite > 0:
            self.stock += quantite
            print(f"Stock ajouté: {quantite}. Nouveau stock: {self.stock}")
        else:
            print("Quantité invalide")

    def retirer_stock(self, quantite):
        """
        Retire une quantité donnée du stock du produit si possible.

        :param quantite: Quantité à retirer
        """
        if quantite <= 0:
            print("Quantité invalide")
        elif quantite > self.stock:
            print("Stock insuffisant")
        else:
            self.stock -= quantite
            print(f"Stock retiré: {quantite}. Nouveau stock: {self.stock}")

    def valeur_stock(self):
        """
        Calcule la valeur totale du stock du produit (HT).

        :return: Valeur du stock (prix HT * quantité)
        """
        return self.prix_ht * self.stock
