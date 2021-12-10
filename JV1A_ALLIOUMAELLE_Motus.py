# Les print de présentation du jeu
print ("--[Vous jouez au jeu Motus ! Pour gagner, vous devez retrouver un mot à partir d'un nombre fixé de lettres. Vous possédez 8 essais avant de perdre la partie... Bonne chance !]--")
print ("(Si la lettre choisie s'affiche en rouge, c'est qu'elle est à la bonne place. En revanche si elle s'affiche en bleu, c'est qu'elle n'appartient pas au mot recherché. Et enfin, si elle s'affiche en jaune, c'est qu'elle est dans le mot mais pas à la bonne place.)")
print ("Commençons !")

# L'accès à Colorama
from colorama import init, Back
init()



# L'importation des mots, des tours, et de la mise en place du tableau
import random
mots = ["Violet", "Carmin", "Indigo", "Acajou", "Corail","Orange", "Pastel", "Marron", "Grenat", "Havane"]
choix = random.choice (mots)
print (choix)

essais=(8)

lettres_tableau = choix
tableau = [0,0,0,0,0,0]
print (tableau)



# Les conditions de victoire/défaite
essais==8

if essais==0 :
    print ('Vous avez perdu la partie, vos 8 essais sont épuisés !')


# Le choix de la lettre (de base avec un "while essais>0" mais qui ne prenait pas en compte la mise en couleur, donc je l'ai enlevé...)
case_choisie = tableau
choix_lettre = input("Choisissez une lettre :")




# Les conditions de mise en couleur rouge, jaune, et bleu des lettres
if choix_lettre in case_choisie and choix :
    print(Back.RED + (choix_lettre)) in tableau
elif choix_lettre in choix :
    print(Back.YELLOW + (choix_lettre))
else :
    print(Back.BLUE + (choix_lettre)) in tableau


input()