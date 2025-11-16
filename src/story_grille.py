# Story: gérer les tirs de l'adversaire sur une grille 5x8
# Étapes:
# 1) créer une grille 5x8
# 2) afficher la grille
# 3) demander (x,y) -> ici (ligne, colonne) en 0-based
# 4) tirer puis retour à 2

from grille import Grille

def run():
    g = Grille(5, 8)
    while True:
        print(g)
        try:
            s = input("Entrez 'ligne colonne' (0-based) ou 'q' : ").strip()
            if s.lower() == "q":
                break
            l_str, c_str = s.split()
            l, c = int(l_str), int(c_str)
        except Exception:
            print("Entrée invalide. Exemple: 2 3")
            continue
        ok = g.tirer(l, c)
        if not ok:
            print("Hors limites !")

if __name__ == "__main__":
    run()