from __future__ import annotations
from typing import List, Tuple

Coord = tuple[int, int]

class Bateau:
    def __init__(self, ligne: int, colonne: int, longueur: int = 1, vertical: bool = False, marque: str = "⛵"):
        self.ligne = int(ligne)
        self.colonne = int(colonne)
        self.longueur = int(longueur)
        self.vertical = bool(vertical)
        self.marque = marque

    @property
    def positions(self) -> List[Coord]:
        """Liste triée des positions (0-based). Par lignes si vertical, par colonnes sinon."""
        if self.vertical:
            return [(self.ligne + k, self.colonne) for k in range(self.longueur)]
        return [(self.ligne, self.colonne + k) for k in range(self.longueur)]

    def coule(self, grille: "Grille", impact: str = "x") -> bool:
        """Vrai si toutes ses cases portent l'impact (par défaut 'x')."""
        from .grille import Grille  # import local pour éviter cycle
        for (l, c) in self.positions:
            if not grille.in_bounds(l, c):
                return False
            if grille.data[grille.index(l, c)] != impact:
                return False
        return True

# Sous-classes typées
class PorteAvion(Bateau):
    def __init__(self, ligne: int, colonne: int, vertical: bool = False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical, marque="🚢")

class Croiseur(Bateau):
    def __init__(self, ligne: int, colonne: int, vertical: bool = False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical, marque="⛴")

class Torpilleur(Bateau):
    def __init__(self, ligne: int, colonne: int, vertical: bool = False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque="🚣")

class SousMarin(Bateau):
    def __init__(self, ligne: int, colonne: int, vertical: bool = False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque="🐟")