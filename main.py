""" Programme principal pour jouer au jeu Quixo """

import api
import quixo
import argparse

def main():
    """
    Fonction principale pour démarrer le jeu Quixo.
    """
    args = quixo.analyser_commande()
    idul = args.idul
    if args.parties:
        parties = api.lister_parties(idul, secret)
        print(quixo.formater_les_parties(parties))
    else:
        id_partie, joueurs, plateau = api.débuter_partie(idul, secret)
        print(quixo.formater_jeu(joueurs, plateau))
        while True:
            origine, direction = quixo.recuperer_le_coup()
            id_partie, joueurs, plateau = api.jouer_coup(id_partie, origine, direction, idul, secret)
            print(quixo.formater_jeu(joueurs, plateau))

if __name__ == "__main__":
    secret = "votre-jeton-personnel"
    main()

