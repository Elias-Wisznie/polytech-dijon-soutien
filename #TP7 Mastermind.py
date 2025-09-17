#TP7 Mastermind

import random


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
    
    couleurs = ['🔴', '🟢', '🔵', '🟡', '🟣', '⚪', '⚫']

    combinaison = []

    #4 couleurs aléatoires, doublons possibles
    for i in range(4):
        couleur_choisie = random.choice(couleurs)
        combinaison.append(couleur_choisie)

    print("vérif :", combinaison)

    return combinaison

def jeu():
    print("Hola")



main()