import copy
from quixo_error import QuixoError


class Plateau:
    """
    Classe représentant le plateau de jeu Quixo.
    """

    def __init__(self, plateau=None):
        """
        Initialise un nouveau plateau de jeu.

        Args:
            plateau (list, optional): Le plateau initial. Defaults to None.
        """
        if plateau is None:
            self.plateau = self.construire_plateau()
        else:
            self.plateau = self.construire_plateau(plateau)

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères du plateau.
        """
        rows = []
        for i, row in enumerate(self.plateau):
            row_str = ' | '.join(row)
            rows.append(f"{i+1} | {row_str} |")
        divider = '-' * (len(rows[0]) - 4)
        return (
            f"   {divider}\n" +
            '\n'.join(rows) +
            f"\n--{divider}--\n  | 1 | 2 | 3 | 4 | 5"
        )

    def __getitem__(self, position):
        """
        Retourne l'élément à la position spécifiée du plateau.

        Args:
            position (tuple): La position de l'élément sous forme (x, y).

        Raises:
            QuixoError: Si les coordonnées spécifiées sont invalides.

        Returns:
            str: L'élément à la position spécifiée du plateau.
        """
        x, y = position
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Les coordonnées spécifiées sont invalides.")
        return self.plateau[x][y]

    def __setitem__(self, position, value):
        """
        Modifie l'élément à la position spécifiée du plateau.

        Args:
            position (tuple): La position de l'élément sous forme (x, y).
            value (str): La valeur à insérer.

        Raises:
            QuixoError: Si les coordonnées spécifiées sont invalides.
        """
        x, y = position
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Les coordonnées spécifiées sont invalides.")
        self.plateau[x][y] = value

    def construire_plateau(self, plateau=None):
        """
        Construit et valide un plateau de jeu.

        Args:
            plateau (list, optional): Le plateau initial. Defaults to None.

        Raises:
            QuixoError: Si le plateau est invalide.

        Returns:
            list: Le plateau construit.
        """
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

    def etat_plateau(self):
        """
        Retourne une copie profonde de l'état du plateau.

        Returns:
            list: Une copie profonde de l'état du plateau.
        """
        return copy.deepcopy(self.plateau)
