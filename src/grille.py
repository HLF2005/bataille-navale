from __future__ import annotations
from typing import List, Tuple
from .utils import Coord

class Grille:
    """
    Grille simulée par une liste 1D de longueur L*C.
    Indices 0-based : (ligne, colonne) -> index = ligne * C + colonne
    """
    def __init__(self, lignes: int, colonnes: int):
        self.L = int(lignes)
        self.C = int(colonnes)
        self.vide = "∿"
        self.tire = "x"   # impact par défaut (exigence "toucher")
        self.data: List[str] = [self.vide] * (self.L * self.C)

    def index(self, l: int, c: int) -> int:
        return l * self.C + c

    def in_bounds(self, l: int, c: int) -> bool:
        return 0 <= l < self.L and 0 <= c < self.C

    def tirer(self, l: int, c: int, touche: str | None = None) -> bool:
        """Marque un tir. Retourne True si dans la grille, False sinon."""
        if not self.in_bounds(l, c):
            return False
        impact = touche if touche is not None else self.tire
        self.data[self.index(l, c)] = impact
        return True

    def ajoute(self, bateau: "Bateau") -> bool:
        """Place un bateau si toutes ses positions tiennent et ne chevauchent pas d'autres bateaux.
        Remplace les cases par bateau.marque. Retourne True si placé, False sinon.
        """
        # 1) Vérif limites
        for (l, c) in bateau.positions:
            if not self.in_bounds(l, c):
                return False
        # 2) Vérif pas de chevauchement (case déjà différente de 'vide' ET pas déjà un tir)
        for (l, c) in bateau.positions:
            cur = self.data[self.index(l, c)]
            if cur != self.vide and cur != self.tire:
                return False
        # 3) Place
        for (l, c) in bateau.positions:
            self.data[self.index(l, c)] = bateau.marque
        return True

    def __str__(self) -> str:
        lines = []
        for l in range(self.L):
            row = "".join(self.data[self.index(l, c)] if self.data[self.index(l, c)] in (self.tire, "💣") or self.data[self.index(l, c)] not in ("🚢","⛴","🚣","🐟","⛵")
                          else self.vide
                          for c in range(self.C))
            # Note: tant que non coulé, on masque les marques des bateaux (révélées à la destruction)
            lines.append(row)
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"Grille({self.L}, {self.C})"