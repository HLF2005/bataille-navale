import pytest
from src.grille import Grille

def test_init():
    g = Grille(5, 8)
    assert g.L == 5 and g.C == 8
    assert len(g.data) == 5*8
    assert all(cell == g.vide for cell in g.data)

def test_indexing_and_tirer():
    g = Grille(5, 8)
    assert g.index(0,0) == 0
    assert g.index(2,3) == 2*8+3
    assert g.tirer(2,3) is True
    assert g.data[g.index(2,3)] == g.tire
    assert g.tirer(99, 0) is False  # hors limites

def test_str_format():
    g = Grille(5, 8)
    before = str(g)
    assert before.splitlines()[0] == "∿"*8
    g.tirer(2,3)
    after = str(g)
    assert after.splitlines()[2][3] == "x"