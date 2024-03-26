# Ce fichier contient les fonctions pour interagir avec le serveur de jeu
import requests

BASE_URL = 'https://pax.ulaval.ca/quixo/api/h24/'

# Fonction pour lister les parties précédentes d'un joueur
     
def lister_parties(idul, secret):

    rep = requests.get(BASE_URL+'parties', auth=(idul, secret))
    if rep.status_code == 200:
        return rep.json()["parties"]
    elif rep.status_code == 401:
        raise PermissionError(rep.json()["message"])
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()["message"])
    else:
        raise ConnectionError

def récupérer_partie(id_partie, idul, secret):
    rep = requests.get(BASE_URL+f'partie/{id_partie}', auth=(idul, secret))
    if rep.status_code == 200:
        data = rep.json()
        return data["id"], data["joueurs"], data["plateau"], data["gagnant"]
    elif rep.status_code == 401:
        raise PermissionError(rep.json()["message"])
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()["message"])
    else:
        raise ConnectionError

def débuter_partie(idul, secret):
    rep = requests.post(BASE_URL+'partie/', auth=(idul, secret))
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
    rep = requests.put(BASE_URL+'jouer/', auth=(idul, secret), json={"id": id_partie, "origine": origine, "direction": direction})
    if rep.status_code == 200:
        data = rep.json()
        return data["id"], data["joueurs"], data["plateau"]
    elif rep.status_code == 401:
        raise PermissionError(rep.json()["message"])
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()["message"])
    else:
        raise ConnectionError
