class Categorie:
    """
    Représente une catégorie de produits dans PyInventory.
    Gère une liste de produits et fournit des propriétés calculées.
    """

    def __init__(self, nom: str, description: str):
        self.nom = nom
        self.description = description
        self._produits = []

    # ---------- propriété nom ----------
    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, valeur: str) -> None:
        if not isinstance(valeur, str) or len(valeur.strip()) < 2:
            raise ValueError("le nom de la catégorie doit contenir au moins 2 caractères")
        self._nom = valeur.strip()

    # ---------- propriétés calculées ----------
    @property
    def nb_produits(self) -> int:
        return len(self._produits)

    @property
    def valeur_totale(self) -> float:
        return sum(p.valeur_stock for p in self._produits)

    @property
    def produits_disponibles(self) -> list:
        return [p for p in self._produits if p.stock > 0]

    # ---------- méthodes ----------
    def ajouter_produit(self, produit) -> None:
        if produit not in self._produits:
            self._produits.append(produit)

    def retirer_produit(self, reference: str) -> bool:
        for p in self._produits:
            if p.reference == reference:
                self._produits.remove(p)
                return True
        return False

    def lister_produits(self) -> None:
        for p in self._produits:
            p.afficher()
