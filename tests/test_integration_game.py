from src.grille import Grille
from src.bateau import Bateau

def test_ajoute_validation():
    g = Grille(2, 3)
    # place horizontal (1,0) longueur 2 -> positions (1,0),(1,1)
    ok = g.ajoute(Bateau(1,0,longueur=2, vertical=False))
    assert ok
    assert g.data == ["∿","∿","∿","⛵","⛵","∿"]

    # invalide (dépasse en vertical)
    g2 = Grille(2,3)
    ok2 = g2.ajoute(Bateau(1,0,longueur=2, vertical=True))
    assert ok2 is False
    assert g2.data == ["∿"]*6

    # invalide (dépasse en horizontal)
    g3 = Grille(2,3)
    ok3 = g3.ajoute(Bateau(1,0,longueur=4, vertical=True))
    assert ok3 is False
    assert g3.data == ["∿"]*6