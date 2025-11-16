# Story: Positionner des bateaux sans chevauchement
# On crée des bateaux et on vérifie s'ils se chevauchent via l'intersection de leurs positions.

from bateau import Bateau
from utils import overlaps

def run():
    b1 = Bateau(2, 3, longueur=3)              # (2,3),(2,4),(2,5)
    b2 = Bateau(2, 5, longueur=2, vertical=True)  # (2,5),(3,5) -> chevauche avec b1
    print("Chevauchent ? ", overlaps(b1.positions, b2.positions))

    b3 = Bateau(0, 0, longueur=2)
    b4 = Bateau(1, 3, longueur=3, vertical=True)
    print("Chevauchent ? ", overlaps(b3.positions, b4.positions))

if __name__ == "__main__":
    run()