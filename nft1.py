#!/usr/bin/python3

from PIL import Image
import random, os

quel_dossier = input("Indiquer dans quel répertoire se trouve le projet ? : ")

X = input("indiquer la couleur du background souhaité : ") # choix de la couleur du fond par l'utilisateur
Y = input("indiquer la forme du visage (carré ou rond) : ") # choix de la forme du visage par l'utilisateur
Q = input("indiquer la couleur du visage : ") # choix de la couleur du visage par l'utilisateur

A = input("Combien de NFT voulez-vous générer ? : ")

for x in range(int(A)): #permet de répéter la boucle le nombre de fois que l'on a choisi dans A

    Z = random.randint(1,9) # génère un nombre entre 1 et 9 pour avoir une coupe de cheveux aléatoire
    V = random.randint(1,20) # génère un nombre entre 1 et 20 pour avoir une bouche aléatoire
    W = random.randint(1,2) # génère un nombre entre 1 et 2 pour avoir des yeux aléatoires
    S = random.randint(1,7) # génère un nombre entre 1 et 7 pour avoir des sourcils aléatoires
    C = random.randint(1,10) # génère un nombre entre 1 et 21 pour avoir des corps aléatoires


    file = "{}/Projet/background/%s.png".format(quel_dossier) % X # récupère les images background
    background = Image.open(file)

    file = "{}/Projet/forme_visage/%s.png".format(quel_dossier) % Y # récupère les formes du visage
    visage = Image.open(file)

    file = "{}/Projet/couleur_visage_rond/%s.png".format(quel_dossier) % Q # récupère les couleurs du visage rond
    couleur_visage_rond = Image.open(file)

    file = "{}/Projet/couleur_visage_carré/%s.png".format(quel_dossier) % Q # récupère les couleurs du visage carré
    couleur_visage_carré = Image.open(file)

    file = "{}/Projet/coiffure_homme_rond/%s.png".format(quel_dossier) % Z # récupère les coiffures homme
    coiffure = Image.open(file)

    file = "{}/Projet/yeux/%s.png".format(quel_dossier) % W # récupère les yeux
    yeux = Image.open(file)
    yeux_size = yeux.size
    yeux = yeux.resize((int(yeux_size[0]/3.0),int(yeux_size[1]/3.0)),Image.ANTIALIAS)

    file = "{}/Projet/corps_homme_couleur_3/%s.png".format(quel_dossier) % C # récupère les vêtements haut du corp
    corp = Image.open(file)
    corp_size = corp.size
    corp = corp.resize((int(corp_size[0]/3.0),int(corp_size[1]/3.0)),Image.ANTIALIAS)

    file = "{}/Projet/bouche/%s.png".format(quel_dossier) % V #récupère la bouvhe
    bouche = Image.open(file)
    bouche_size = bouche.size
    bouche = bouche.resize((int(bouche_size[0]/4.0),int(bouche_size[1]/4.0)),Image.ANTIALIAS)

    file = "{}/Projet/sourcil/%s.png".format(quel_dossier) % S # récupère les sourcil
    sourcil = Image.open(file)
    sourcil_size = sourcil.size
    sourcil = sourcil.resize((int(sourcil_size[0]/3.5),int(sourcil_size[1]/4.0)),Image.ANTIALIAS)


    if C == 1 :
        background.paste(corp, (60,155), mask = corp) # permet de mettre en background la couleur choisi au début et de rajouter le corp par dessus au position -110,20
    if C == 2 :
        background.paste(corp, (88,200), mask = corp)
    if C == 3 :
        background.paste(corp, (100,200), mask = corp)
    if C == 4 :
        background.paste(corp, (100,102), mask = corp)
    if C == 5 :
        background.paste(corp, (78,190), mask = corp)
    if C == 6 :
        background.paste(corp, (110,185), mask = corp)
    if C == 7 :
        background.paste(corp, (102,195), mask = corp)
    if C == 8 :
        background.paste(corp, (105,180), mask = corp)
    if C == 9 :
        background.paste(corp, (108,190), mask = corp)
    if C == 10 :
        background.paste(corp, (100,195), mask = corp)
        
    #background.paste(visage, (0,-60), mask = visage) # de même mais avec le visage carré ou rond en position 0,-60

    if Y == "rond" : # sachant que chaque coupe est différente, elle leur faut à chacune une position spécifique

        background.paste(couleur_visage_rond, (110,50), mask = couleur_visage_rond)
        
    
    ############################################################
    #                            Yeux rond
    ############################################################
        if W == 1 :
            background.paste(yeux, (107,92), mask = yeux)
            if S == 1 :
                background.paste(sourcil, (115,87), mask = sourcil)
            if S == 2 :
                background.paste(sourcil, (97,75), mask = sourcil)
            if S == 3 :
                background.paste(sourcil, (102,72), mask = sourcil)
            if S == 4 :
                background.paste(sourcil, (102,75), mask = sourcil)
            if S == 5 :
                background.paste(sourcil, (100,80), mask = sourcil)
            if S == 6 :
                background.paste(sourcil, (120,95), mask = sourcil)
            if S == 7 :
                background.paste(sourcil, (105,80), mask = sourcil)
        if W == 2 :
            background.paste(yeux, (100,100), mask = yeux)
            if S == 1 :
                background.paste(sourcil, (115,70), mask = sourcil)
            if S == 2 :
                background.paste(sourcil, (102,62), mask = sourcil)
            if S == 3 :
                background.paste(sourcil, (105,60), mask = sourcil)
            if S == 4 :
                background.paste(sourcil, (105,63), mask = sourcil)
            if S == 5 :
                background.paste(sourcil, (100,66), mask = sourcil)
            if S == 6 :
                background.paste(sourcil, (125,80), mask = sourcil)
            if S == 7 :
                background.paste(sourcil, (110,68), mask = sourcil)
    ############################################################
    #                     Coiffure visage rond homme
    ############################################################
        if Z == 1 : # nom des différentes coupes qui sont choisis aléatoirement
            background.paste(coiffure, (49,-35), mask = coiffure) # rajout de la coupe sur le background 
        if Z == 2 :
            background.paste(coiffure, (52,-10), mask = coiffure)
        if Z == 3 :
            background.paste(coiffure, (30,-35), mask = coiffure)
        if Z == 4 :
            background.paste(coiffure, (50,-14), mask = coiffure)
        if Z == 5 :
            background.paste(coiffure, (-20,-40), mask = coiffure)
        if Z == 6 :
            background.paste(coiffure, (42,-15), mask = coiffure)
        if Z == 7 :
            background.paste(coiffure, (40,-60), mask = coiffure)
        if Z == 8 :
            background.paste(coiffure, (63,-40), mask = coiffure)
        if Z == 9 :
            background.paste(coiffure, (45,-40), mask = coiffure)
    ############################################################
    #                     Bouche visage rong
    ############################################################
        if V == 1 or V == 2 or V == 3 or V == 11 or V == 12 or V == 13 :
            background.paste(bouche, (140,145), mask = bouche)        
        if V == 4 :
            background.paste(bouche, (130,135), mask = bouche)
        if V == 5 or V == 6 or V == 7 or V == 15 or V == 14 :
            background.paste(bouche, (123,145), mask = bouche)
        if V == 9 or V == 16 or V == 17 :
            background.paste(bouche, (140,140), mask = bouche)
        if V == 8 :
            background.paste(bouche, (160,145), mask = bouche)
        if V == 19 :
            background.paste(bouche, (140,150), mask = bouche)
        if V == 18 :
            background.paste(bouche, (120,130), mask = bouche)
        if V == 20 :
            background.paste(bouche, (140,155), mask = bouche)
        if V == 10 :
            background.paste(bouche, (150,155), mask = bouche)



            
    if Y == "carré" : # même chose mais avec la tête carré

        background.paste(couleur_visage_carré, (120,50), mask = couleur_visage_carré)
    ############################################################
    #                            Yeux carré
    ############################################################
        if W == 1 :
            background.paste(yeux, (110,80), mask = yeux)
            if S == 1 :
                background.paste(sourcil, (115,70), mask = sourcil)
            if S == 2 :
                background.paste(sourcil, (100,60), mask = sourcil)
            if S == 3 :
                background.paste(sourcil, (105,60), mask = sourcil)
            if S == 4 :
                background.paste(sourcil, (103,65), mask = sourcil)
            if S == 5 :
                background.paste(sourcil, (100,65), mask = sourcil)
            if S == 6 :
                background.paste(sourcil, (125,85), mask = sourcil)
            if S == 7 :
                background.paste(sourcil, (110,70), mask = sourcil)
        if W == 2 :
            background.paste(yeux, (100,100), mask = yeux)
            if S == 1 :
                background.paste(sourcil, (115,70), mask = sourcil)
            if S == 2 :
                background.paste(sourcil, (102,62), mask = sourcil)
            if S == 3 :
                background.paste(sourcil, (105,60), mask = sourcil)
            if S == 4 :
                background.paste(sourcil, (105,63), mask = sourcil)
            if S == 5 :
                background.paste(sourcil, (100,66), mask = sourcil)
            if S == 6 :
                background.paste(sourcil, (125,80), mask = sourcil)
            if S == 7 :
                background.paste(sourcil, (110,68), mask = sourcil)
        
    ############################################################
    #                     Coiffure visage carré homme
    ############################################################
        if Z == 1 : # nom des différentes coupes qui sont choisis aléatoirement
            background.paste(coiffure, (49,-40), mask = coiffure) # rajout de la coupe sur le background 
        if Z == 2 :
            background.paste(coiffure, (42,-14), mask = coiffure)
        if Z == 3 :
            background.paste(coiffure, (30,-35), mask = coiffure)
        if Z == 4 :
            background.paste(coiffure, (50,-14), mask = coiffure)
        if Z == 5 :
            background.paste(coiffure, (-20,-40), mask = coiffure)
        if Z == 6 :
            background.paste(coiffure, (40,-27), mask = coiffure)
        if Z == 7 :
            background.paste(coiffure, (40,-60), mask = coiffure)
        if Z == 8 :
            background.paste(coiffure, (63,-40), mask = coiffure)
        if Z == 9 :
            background.paste(coiffure, (32,-60), mask = coiffure)
            
    ############################################################
    #                     Bouche visage carré homme
    ############################################################
        if V == 1 or V == 11 or V == 12 or V == 13 :
            background.paste(bouche, (140,145), mask = bouche)
        if V == 2 :
            background.paste(bouche, (140,135), mask = bouche)
        if V == 3 :
            background.paste(bouche, (145,144), mask = bouche)
        if V == 4 :
            background.paste(bouche, (127,127), mask = bouche)
        if V == 5 or V == 6 :
            background.paste(bouche, (123,145), mask = bouche)
        if V == 7 or V == 15 or V == 14 :
            background.paste(bouche, (123,135), mask = bouche)
        if V == 9 or V == 16 :
            background.paste(bouche, (140,140), mask = bouche)
        if V == 17 :
            background.paste(bouche, (145,140), mask = bouche)
        if V == 8 :
            background.paste(bouche, (160,145), mask = bouche)
        if V == 19 :
            background.paste(bouche, (145,150), mask = bouche)
        if V == 18 :
            background.paste(bouche, (115,125), mask = bouche)
        if V == 20 :
            background.paste(bouche, (140,155), mask = bouche)
        if V == 10 :
            background.paste(bouche, (150,145), mask = bouche)
    ############################################################
    

    background.show() #affiche le background avec tout les élements rajouter par dessus ( visage, corp etc...)
