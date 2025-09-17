#TP7 Mastermind

import random


def generer_combinaison():
    
    couleurs = ['🔴', '🟢', '🔵', '🟡', '🟣', '⚪', '⚫']

    combinaison = []

    #4 couleurs aléatoires, doublons possibles
    for i in range(4):
        couleur_choisie = random.choice(couleurs)
        combinaison.append(couleur_choisie)

    print("vérif :", combinaison)

    return combinaison

generer_combinaison()
