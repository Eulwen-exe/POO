class Produit:
    # attributs de classe
    tva = 20
    nb_produits = 0

    def __init__(self, reference, nom, prix_ht, stock):
        # passer par les setters (important)
        self.reference = reference
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock

        Produit.nb_produits += 1

    # --- reference ---
    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, valeur):
        if not isinstance(valeur, str):
            raise TypeError("reference doit être une chaîne de caractères")
        valeur = valeur.strip()
        if len(valeur) < 3:
            raise ValueError("reference doit contenir au moins 3 caractères")
        self._reference = valeur.upper()

    # --- nom ---
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        if not isinstance(valeur, str):
            raise TypeError("nom doit être une chaîne de caractères")
        valeur = valeur.strip()
        if len(valeur) < 2:
            raise ValueError("nom doit contenir au moins 2 caractères")
        self._nom = valeur

    # --- prix_ht ---
    @property
    def prix_ht(self):
        return self._prix_ht

    @prix_ht.setter
    def prix_ht(self, valeur):
        if not isinstance(valeur, (int, float)) or isinstance(valeur, bool):
            raise TypeError("prix_ht doit être un nombre (int ou float)")
        if valeur <= 0:
            raise ValueError("prix_ht doit être strictement positif")
        self._prix_ht = round(float(valeur), 2)

    # --- stock ---
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valeur):
        if not isinstance(valeur, int) or isinstance(valeur, bool):
            raise TypeError("stock doit être un entier")
        if valeur < 0:
            raise ValueError("stock doit être positif ou nul")
        self._stock = valeur

    # --- propriétés calculées ---
    @property
    def prix_ttc(self):
        return round(self.prix_ht * (1 + Produit.tva / 100), 2)

    @property
    def valeur_stock(self):
        return round(self.prix_ht * self.stock, 2)

    # --- méthodes ---
    def ajouter_stock(self, quantite):
        if not isinstance(quantite, int) or isinstance(quantite, bool):
            raise TypeError("quantite doit être un entier")
        if quantite <= 0:
            raise ValueError("quantite doit être strictement positive")
        self.stock = self.stock + quantite
        print(f"Stock: {self.stock}")

    def retirer_stock(self, quantite):
        if not isinstance(quantite, int) or isinstance(quantite, bool):
            raise TypeError("quantite doit être un entier")
        if quantite <= 0:
            raise ValueError("quantite doit être strictement positive")
        if quantite > self.stock:
            raise ValueError("stock insuffisant")
        self.stock = self.stock - quantite
        print(f"Stock: {self.stock}")


p = Produit("kb-001", "Clavier RGB", 79.99, 15)
print(p.reference)  # KB-001
print(p.prix_ttc)   # 95.99

p.prix_ht = 69.99
p.ajouter_stock(10)  # Stock: 25
p.retirer_stock(5)   # Stock: 20

