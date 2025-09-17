#TP7 Mastermind

import random
import os

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

    os.system('cls')

    print("\nCouleurs disponibles :")
    print("🔴 = R | 🟢 = G | 🔵 = B | 🟡 = Y | 🟣 = P | ⚪ = W | ⚫ = K")
    print("Entrez une combinaison de 4 lettres (exemple : RBYK)")
    print("L'objectif est de trouver la combinaison cachée en 12 tentatives")

    combinaison = generer_combinaison()

    n = 12

    for i in range(n):
        
        try:
            rep = int(input("Saisissez une combinaison : "))





main()