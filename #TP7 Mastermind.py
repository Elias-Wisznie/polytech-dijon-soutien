# TP7 Mastermind

#To do:
#Save score et nbr parties dans un txt
#Lire ce txt au setup pour récup les stats


import random
import os

# Liste des couleurs disponibles
couleurs_disponibles = ["R", "G", "B", "Y", "P", "W", "K"]

longueur_combinaison = 4 # nombre d'éléments du code secret 
tentatives_max = 12 #nombre maximum de tentatives
nbr_parties_jouees = 0 #nombre de parties qui ont été lancées au total
score = 0 #score du joueur, +1pt à chaque partie gagnée



# chemin du fichier de stats sur le bureau 
fichier_stats = os.path.join(os.path.expanduser("~"), "Desktop", "mastermind_stats.txt")







def charger_stats():
    global nbr_parties_jouees, score
    try:
        with open(fichier_stats, "r") as f:
            lignes = f.readlines()
            nbr_parties_jouees = int(lignes[0].strip())
            score = int(lignes[1].strip())
    except:
        nbr_parties_jouees = 0
        score = 0

def sauvegarder_stats():
    with open(fichier_stats, "w") as f:
        f.write(str(nbr_parties_jouees) + "\n")
        f.write(str(score) + "\n")







def main():
    
    global longueur_combinaison

    # charger stats au lancement
    charger_stats()

    print(" *** Jeu du Mastermind ***")
    print(f"Parties jouées : {nbr_parties_jouees} | Score : {score}\n")

    while True:
        print("Sélectionnez une option de jeu")
        print("Couleur aléatoire : 1 | Sélection manuelle de la couleur à trouver : 2 | Choisir la longueur du code secret : 3")

        try:
            menu = int(input("Saisissez un nombre : "))
            if menu == 1:
                jeu()
                # sauvegarder stats après chaque partie
                sauvegarder_stats()
            elif menu == 2:
                print("Mode en développement")
            elif menu == 3:
                try:
                    choix = int(input(f"Entrez la longueur du code secret (2 à {len(couleurs_disponibles)}) : "))
                    if 2 <= choix <= len(couleurs_disponibles): #pas de long que le nombre de couleurs dispo (7) parce qu'il faut sinon changer des choses dans le reste du programme
                        longueur_combinaison = choix
                        print(f"Longueur du code secret définie à {longueur_combinaison}")
                    else:
                        print("Valeur invalide, gardons la valeur actuelle.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
            else:
                print("Choix invalidé, veuillez choisir 1, 2 ou 3.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")





# le reste du code reste identique à ton script original
def generer_combinaison():
    
    # couleurs aléatoires, doublons possibles
    combinaison = [random.choice(couleurs_disponibles) for _ in range(longueur_combinaison)]

    print("vérif :", combinaison)  # affichage debug pour vérifier la combinaison générée

    return combinaison






def conversion_reponse(reponse_joueur): 
    # Converti la réponse du joueur en quelque chose de comparable avec la combinaison générée

    combinaison_convertie = []
    for lettre in reponse_joueur.upper(): #upper mettre en maj
        if lettre in couleurs_disponibles:
            combinaison_convertie.append(lettre)
    return combinaison_convertie






def comparaison(combinaison, proposition):  
    # Comparaison de la réponse de l'utilisateur pour indiquer combien sont bien ou mal placés

    bien_places = 0
    mal_places = 0

    copie_combinaison = combinaison.copy()
    copie_proposition = proposition.copy()

    # Etape 1 compter les bien placés
    for i in range(longueur_combinaison):
        if copie_proposition[i] == copie_combinaison[i]:
            bien_places += 1
            copie_combinaison[i] = None  # on marque pour ne plus la compter
            copie_proposition[i] = None

    # Etape 2 compter les mal placés
    for i in range(longueur_combinaison):
        if copie_proposition[i] is not None and copie_proposition[i] in copie_combinaison:
            mal_places += 1
            # on enleve cette couleur de la liste pourpas la compter deux fois
            copie_combinaison[copie_combinaison.index(copie_proposition[i])] = None

    return bien_places, mal_places






def jeu():  # là où se passe le gameplay

    global score
    global nbr_parties_jouees

    os.system('cls')

    nbr_parties_jouees = nbr_parties_jouees + 1

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
            score = score + 1
            return


main()
