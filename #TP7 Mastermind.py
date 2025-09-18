# TP7 Mastermind

import random
import os

# Liste des couleurs disponibles
couleurs_disponibles = ["R", "G", "B", "Y", "P", "W", "K"]


longueur_combinaison = 4   # nombre d'éléments du code secret 
tentatives_max = 12        # nombre maximum de tentatives




def main():
    
    global longueur_combinaison

    print(" *** Jeu du Mastermind ***")

    while True:
        print("Sélectionnez une option de jeu")
        print("Couleur aléatoire : 1 | Sélection manuelle de la couleur à trouver : 2 | Choisir la longueur du code secret : 3")

        try:
            menu = int(input("Saisissez un nombre : "))
            if menu == 1:
                jeu()
            elif menu == 2:
                print("Mode en développement")
            elif menu == 3:
                try:
                    choix = int(input(f"Entrez la longueur du code secret (2 à {len(couleurs_disponibles)}) : "))
                    if 2 <= choix <= len(couleurs_disponibles):
                        longueur_combinaison = choix
                        print(f"Longueur du code secret définie à {longueur_combinaison}")
                    else:
                        print("Valeur invalide, gardons la valeur actuelle.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
            else:
                print("Choix invalide ! Veuillez choisir 1, 2 ou 3.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")




def generer_combinaison():
    
    # couleurs aléatoires, doublons possibles
    combinaison = [random.choice(couleurs_disponibles) for _ in range(longueur_combinaison)]

    print("vérif :", combinaison)  # affichage debug pour vérifier la combinaison générée

    return combinaison






def conversion_reponse(reponse_joueur): 
    # Converti la réponse du joueur en quelque chose de comparable avec la combinaison générée

    combinaison_convertie = []
    for lettre in reponse_joueur.upper():
        if lettre in couleurs_disponibles:
            combinaison_convertie.append(lettre)
    return combinaison_convertie





def comparaison(combinaison, proposition):  
    # Comparaison de la réponse de l'utilisateur pour lui indiquer combien sont bien ou mal placés

    bien_places = 0
    mal_places = 0

    copie_combinaison = combinaison.copy()
    copie_proposition = proposition.copy()

    # Étape 1 : compter les bien placés
    for i in range(longueur_combinaison):
        if copie_proposition[i] == copie_combinaison[i]:
            bien_places += 1
            copie_combinaison[i] = None  # on marque pour ne plus la compter
            copie_proposition[i] = None

    # Étape 2 : compter les mal placés
    for i in range(longueur_combinaison):
        if copie_proposition[i] is not None and copie_proposition[i] in copie_combinaison:
            mal_places += 1
            # on enlève cette couleur de la liste pour éviter de la compter deux fois
            copie_combinaison[copie_combinaison.index(copie_proposition[i])] = None

    return bien_places, mal_places





def jeu():  # là où se passe le gameplay

    os.system('cls')

    print("\nCouleurs disponibles :")
    print("R = Rouge | G = Vert | B = Bleu | Y = Jaune | P = Violet | W = Blanc | K = Noir")
    print(f"Entrez une combinaison de {longueur_combinaison} lettres (exemple : RBYK)")
    print(f"L'objectif est de trouver la combinaison cachée en {tentatives_max} tentatives")

    combinaison = generer_combinaison()

    n = tentatives_max

    for essai in range(1, n+1):
        rep = input(f"Tentative {essai}/{n} : ")

        essai_converti = conversion_reponse(rep)

        if len(essai_converti) != longueur_combinaison:
            print(f"Saisie invalide, utilisez exactement {longueur_combinaison} lettres valides")
            continue

        bien, mal = comparaison(combinaison, essai_converti)

        print("Votre proposition :", essai_converti)
        print(f"Indices - Bien placés: {bien}, Mal placés: {mal}\n")

        if bien == longueur_combinaison:
            print("Vous avez trouvé la combinaison")
            return

    print("Vous avez épuisé vos tentatives. La combinaison était :", combinaison)


main()
