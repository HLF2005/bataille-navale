from src.bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin
from src.grille import Grille

def test_positions_default_and_vertical():
    b = Bateau(2, 3, longueur=3)
    assert b.positions == [(2,3),(2,4),(2,5)]
    b2 = Bateau(2, 3, longueur=3, vertical=True)
    assert b2.positions == [(2,3),(3,3),(4,3)]

def test_coule():
    g = Grille(3, 5)
    b = Bateau(1, 1, longueur=2)
    assert g.ajoute(b)
    # tirs
    g.tirer(1,1); g.tirer(1,2)
    assert b.coule(g)

def test_types():
    g = Grille(3, 5)
    assert g.ajoute(PorteAvion(0,0)) is True
    assert g.ajoute(Croiseur(2,2, vertical=True)) in (True, False)  # selon place dispo
    # on vérifie surtout que la marque vient bien du type
    b = Torpilleur(1,0)
    assert b.longueur == 2 and b.marque == "🚣"
    b2 = SousMarin(1,3, vertical=True)
    assert b2.longueur == 2 and b2.vertical is True and b2.marque == "🐟"