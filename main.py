from Produits import Produit
from Categorie import Categorie

p1 = Produit("KB-001", "Clavier mécanique RGB", 79.99, 15)
p2 = Produit("MS-002", "Souris gaming 16000 DPI", 49.99, 25)


p1.ajouter_stock(5)
p1.afficher()
p1.retirer_stock(2)
p1.afficher()
print(p1.valeur_stock())
p2.ajouter_stock(10)
p2.afficher()
p2.retirer_stock(5)
p2.afficher()
print(p2.valeur_stock())

print(f"Total produits: {Produit.nb_produits}")