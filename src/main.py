import random
from typing import List, Tuple
from src.grille import Grille
from src.bateau import PorteAvion, Croiseur, Torpilleur, SousMarin, Bateau

def placements_possibles(g: Grille, longueur: int, marque: str) -> List[Tuple[int,int,bool]]:
    """Retourne toutes les (l,c,vertical) possibles sans chevauchement pour un bateau de longueur donnée."""
    possibles = []
    # horizontal
    for l in range(g.L):
        for c in range(g.C - longueur + 1):
            ok = True
            for k in range(longueur):
                cell = g.data[g.index(l, c + k)]
                if cell != g.vide and cell != g.tire:
                    ok = False; break
            if ok:
                possibles.append((l, c, False))
    # vertical
    for l in range(g.L - longueur + 1):
        for c in range(g.C):
            ok = True
            for k in range(longueur):
                cell = g.data[g.index(l + k, c)]
                if cell != g.vide and cell != g.tire:
                    ok = False; break
            if ok:
                possibles.append((l, c, True))
    return possibles

def place_flotte_aleatoire(g: Grille, rng: random.Random) -> List[Bateau]:
    flotte: List[Bateau] = []
    types = [(PorteAvion, 4), (Croiseur, 3), (Torpilleur, 2), (SousMarin, 2)]
    for cls, L in types:
        cand = placements_possibles(g, L, "?")
        if not cand:
            # échec de placement (rare) -> reset et recommence
            return place_flotte_aleatoire(Grille(g.L, g.C), rng)
        l, c, vertical = rng.choice(cand)
        b = cls(l, c, vertical=vertical)
        assert g.ajoute(b), "Placement devrait réussir"
        flotte.append(b)
    return flotte

def nom_bateau(b: Bateau) -> str:
    return {
        "🚢":"Porte-avions",
        "⛴":"Croiseur",
        "🚣":"Torpilleur",
        "🐟":"Sous-marin",
    }.get(b.marque, "Bateau")

def message_coule(b: Bateau) -> str:
    return {
        "🚢":"Le porte-avions sombre majestueusement !",
        "⛴":"Le croiseur est coulé !",
        "🚣":"Torpilleur neutralisé.",
        "🐟":"Sous-marin hors d'état !",
    }.get(b.marque, "Bateau coulé !")

def reveler_bateau(g: Grille, b: Bateau):
    for (l, c) in b.positions:
        g.data[g.index(l, c)] = b.marque

def main():
    rng = random.Random()
    g = Grille(8, 10)
    flotte = place_flotte_aleatoire(g, rng)
    print("=== Bataille navale ===")
    coups = 0
    coules = set()

    while True:
        print()
        print(g)
        s = input("Tir (ligne colonne en 0-based) ou q: ").strip()
        if s.lower() == "q":
            print("À bientôt !")
            break
        try:
            l_str, c_str = s.split()
            l, c = int(l_str), int(c_str)
        except Exception:
            print("Entrée invalide. Exemple: 2 3")
            continue

        if not g.in_bounds(l, c):
            print("Hors limites.")
            continue

        coups += 1
        # Tir d'abord avec 💣 pour signaler un impact visible
        g.tirer(l, c, touche="💣")

        # Vérifier si on a touché un bateau (impact sur une case où il y avait un bateau masqué)
        touche_quelque_chose = False
        for b in flotte:
            if (l, c) in b.positions:
                touche_quelque_chose = True
                break
        print("Touché !" if touche_quelque_chose else "Plouf !")

        # Remettre les 💣 en 'x' pour le suivi (impact permanent)
        if g.data[g.index(l, c)] == "💣":
            g.data[g.index(l, c)] = g.tire

        # Vérifier les coulés
        for b in flotte:
            if b in coules:
                continue
            if b.coule(g, impact=g.tire):
                print(message_coule(b))
                reveler_bateau(g, b)
                coules.add(b)

        if len(coules) == len(flotte):
            print()
            print(g)
            print(f"Victoire en {coups} coups !")
            break

if __name__ == "__main__":
    main()
