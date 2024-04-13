import requests


BASE_URL = 'https://pax.ulaval.ca/quixo/api/h24/'


def lister_parties(idul, secret):
    """
    Fonction pour lister les parties précédentes d'un joueur.

    Args:
        idul (str): L'IDUL du joueur.
        secret (str): Le jeton secret du joueur.

    Returns:
        list: Liste des parties précédentes du joueur.
    """
    rep = requests.get(BASE_URL + 'parties', auth=(idul, secret))
    if rep.status_code == 200:
        return rep.json()["parties"]
    elif rep.status_code == 401:
        raise PermissionError(rep.json()["message"])
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()["message"])
    else:
        raise ConnectionError


def recuperer_partie(id_partie, idul, secret):
    """
    Fonction pour récupérer une partie spécifique.

    Args:
        id_partie (str): L'identifiant de la partie à récupérer.
        idul (str): L'IDUL du joueur.
        secret (str): Le jeton secret du joueur.

    Returns:
        tuple: ID de la partie, joueurs, plateau, gagnant.
    """
    rep = requests.get(BASE_URL + f'partie/{id_partie}', auth=(idul, secret))
    if rep.status_code == 200:
        data = rep.json()
        return data["id"], data["joueurs"], data["plateau"], data["gagnant"]
    elif rep.status_code == 401:
        raise PermissionError(rep.json()["message"])
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()["message"])
    else:
        raise ConnectionError


def debuter_partie(idul, secret):
    """
    Fonction pour démarrer une nouvelle partie.

    Args:
        idul (str): L'IDUL du joueur.
        secret (str): Le jeton secret du joueur.

    Returns:
        tuple: ID de la partie, joueurs, plateau.
    """
    rep = requests.post(BASE_URL + 'partie/', auth=(idul, secret))
    if rep.status_code == 200:
        data = rep.json()
        return data["id"], data["joueurs"], data["plateau"]
    elif rep.status_code == 401:
        raise PermissionError(rep.json()["message"])
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()["message"])
    else:
        raise ConnectionError


def jouer_coup(id_partie, origine, direction, idul, secret):
    """
    Fonction pour jouer un coup dans une partie.

    Args:
        id_partie (str): L'identifiant de la partie.
        origine (tuple): La position d'origine du coup.
        direction (str): La direction du coup.
        idul (str): L'IDUL du joueur.
        secret (str): Le jeton secret du joueur.

    Returns:
        tuple: ID de la partie, joueurs, plateau.
    """
    rep = requests.put(BASE_URL + 'jouer/', auth=(idul, secret), json={
                       "id": id_partie, "origine": origine, "direction": direction})
    if rep.status_code == 200:
        data = rep.json()
        return data["id"], data["joueurs"], data["plateau"]
    elif rep.status_code == 401:
        raise PermissionError(rep.json()["message"])
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()["message"])
    else:
        raise ConnectionError
