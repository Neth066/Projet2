import copy
from quixo_error import QuixoError

class Plateau:
    def __init__(self, plateau=None):
        if plateau is None:
            self.plateau = self.construire_plateau()
        else:
            self.plateau = self.construire_plateau(plateau)

    def __str__(self):
        rows = []
        for i, row in enumerate(self.plateau):
            row_str = ' | '.join(row)
            rows.append(f"{i+1} | {row_str} |")
        divider = '-' * (len(rows[0]) - 4)
        return f"   {divider}\n" + '\n'.join(rows) + f"\n--{divider}--\n  | 1 | 2 | 3 | 4 | 5"

    def __getitem__(self, position):
        x, y = position
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Les coordonnées spécifiées sont invalides.")
        return self.plateau[x][y]

    def __setitem__(self, position, value):
        x, y = position
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Les coordonnées spécifiées sont invalides.")
        self.plateau[x][y] = value

    def construire_plateau(self, plateau=None):
        if plateau is None:
            return [[' ']*5 for _ in range(5)]
        else:
            if len(plateau) != 5 or any(len(row) != 5 for row in plateau):
                raise QuixoError("Le plateau doit être une liste de 5 listes de 5 éléments.")
            for row in plateau:
                for element in row:
                    if element not in ['X', 'O', ' ']:
                        raise QuixoError("Le plateau ne peut contenir que des 'X', des 'O' ou des espaces.")
            return plateau

    def état_plateau(self):
        return copy.deepcopy(self.plateau)

    def insertion_par_le_bas(self, pion, origine):
        x, y = origine
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Les coordonnées spécifiées sont invalides.")
        if self.plateau[4][y] != ' ':
            raise QuixoError("Impossible d'insérer un pion par le bas à cette position.")
        for i in range(4, 0, -1):
            self.plateau[i][y] = self.plateau[i-1][y]
        self.plateau[0][y] = pion

    def insertion_par_le_haut(self, pion, origine):
        x, y = origine
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Les coordonnées spécifiées sont invalides.")
        if self.plateau[0][y] != ' ':
            raise QuixoError("Impossible d'insérer un pion par le haut à cette position.")
        for i in range(4):
            self.plateau[i][y] = self.plateau[i+1][y]
        self.plateau[4][y] = pion

    def insertion_par_la_gauche(self, pion, origine):
        x, y = origine
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Les coordonnées spécifiées sont invalides.")
        if self.plateau[x][0] != ' ':
            raise QuixoError("Impossible d'insérer un pion par la gauche à cette position.")
        for i in range(4):
            self.plateau[x][i] = self.plateau[x][i+1]
        self.plateau[x][4] = pion

    def insertion_par_la_droite(self, pion, origine):
        x, y = origine
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Les coordonnées spécifiées sont invalides.")
        if self.plateau[x][4] != ' ':
            raise QuixoError("Impossible d'insérer un pion par la droite à cette position.")
        for i in range(4, 0, -1):
            self.plateau[x][i] = self.plateau[x][i-1]
        self.plateau[x][0] = pion

    def insertion(self, pion, origine, direction):
        if direction == 'haut':
            self.insertion_par_le_haut(pion, origine)
        elif direction == 'bas':
            self.insertion_par_le_bas(pion, origine)
        elif direction == 'gauche':
            self.insertion_par_la_gauche(pion, origine)
        elif direction == 'droite':
            self.insertion_par_la_droite(pion, origine)
        else:
            raise QuixoError("Direction invalide.")
