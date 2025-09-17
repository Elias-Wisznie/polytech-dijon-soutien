#TP7 Mastermind

import random
import os

# dictionnaire pour faire la conversion lettre en emoji
map_couleurs = {
    "R": "🔴",
    "G": "🟢",
    "B": "🔵",
    "Y": "🟡",
    "P": "🟣",
    "W": "⚪",
    "K": "⚫"
}


def main():
    
    print(" *** Jeu du Mastermind ***")

    while True:
        print("Sélectionnez une option de jeu")
        print("Couleur aléatoire : 1 | Sélection manuelle de la couleur à trouver : 2")

        try:
            menu = int(input("Saisissez un nombre : "))
            if menu == 1:
                jeu()
            elif menu == 2:
                print("Mode en développement")
            else:
                print("Choix invalide ! Veuillez choisir 1 ou 2.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")





def generer_combinaison():
    
    couleurs = list(map_couleurs.values())

    combinaison = []

    #4 couleurs aléatoires, doublons possibles
    for i in range(4):
        couleur_choisie = random.choice(couleurs)
        combinaison.append(couleur_choisie)

    print("vérif :", combinaison)

    return combinaison


def conversion_reponse(reponse_joueur): #Converti la réponse du jour en quelque chose de comparable avec la combinaison générée
    
    combinaison_convertie = []
    for lettre in reponse_joueur.upper():
        if lettre in map_couleurs:
            combinaison_convertie.append(map_couleurs[lettre])
    return combinaison_convertie


def comparaison(): #Comparaison de la réponse de l'utilisateur pour lui indiquer combien sont bien ou mal placés






def jeu(): #là où se passe le gameplay

    os.system('cls')

    print("\nCouleurs disponibles :")
    print("🔴 = R | 🟢 = G | 🔵 = B | 🟡 = Y | 🟣 = P | ⚪ = W | ⚫ = K")
    print("Entrez une combinaison de 4 lettres (exemple : RBYK)")
    print("L'objectif est de trouver la combinaison cachée en 12 tentatives")

    combinaison = generer_combinaison()

    n = 12

    for essai in range(n, n+1):
        rep = input(("Saisissez votre combinaison:"))

        essai_converti = conversion_reponse(rep)

        if len(essai_converti) != 4:
            print("Saisie invalide, utilisez 4 lettres")
            continue





main()