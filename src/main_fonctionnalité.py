# À réécrire à chaque nouvelle feature pour "jouer" rapidement avec la fonctionnalité.
from grille import Grille

if __name__ == "__main__":
    g = Grille(5, 8)
    print(g)
    g.tirer(2, 3)
    print(g)