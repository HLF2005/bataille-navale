# Bataille navale — version simplifiée

- **Indices 0-based**: `tirer(ligne, colonne)` utilise des indices à partir de 0.
- **Boucle de dev** : vérif rapide dans `main_fonctionnalité.py` → conversion en tests `pytest`.
- **Jeu final** : `src/main.py`.

## Installation
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt

Lancer les tests
pytest -q

Lancer le jeu
python -m src.main

UML (résumé)
	•	Grille(lignes:int, colonnes:int)
	•	attrs: L, C, data:list[str], vide='∿', touche='x'
	•	ops: index(l,c)->int, in_bounds(l,c)->bool, tirer(l,c, touche='x'), ajoute(bateau), __str__()
	•	Bateau(ligne:int, colonne:int, longueur:int=1, vertical:bool=False)
	•	attrs: ligne, colonne, longueur, vertical, marque='⛵'
	•	prop: positions -> list[tuple[int,int]]
	•	ops: coule(grille:'Grille')->bool
	•	Spécialisations: PorteAvion(4, "🚢"), Croiseur(3, "⛴"), Torpilleur(2, "🚣"), SousMarin(2, "🐟")

Règles
	•	Grille 8x10
	•	4 bateaux (un de chaque type), placement aléatoire sans chevauchement.
	•	Tir : affichage 💣 sur impact. Si coulé, le bateau est révélé sur la grille avec sa marque.
	•	Fin : quand tous les bateaux sont coulés; on affiche le nombre de coups.


---

