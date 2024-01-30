from getpass import getpass
mot = getpass(" joueur 1 veuillez saisir le mot secret: ")
tentatives = 7
affichage = ""
lettres_trouvees = ""

for l in mot:
  affichage = affichage + "_ "

print(">> Bienvenue dans le pendu <<")

while tentatives > 0:                                       #ici on dit que temps que le nombre de tentative restante est supérieur à 0 alors le jeu continue
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")[0:1].lower()

 
  if proposition in mot:                                    #on définit ici que si la proposition du joueur est une partie du mot alors on lui dis que c'est bon
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:                                                     #sinon ici on affiche que c'est raté et que de faites on affiche le pendu
    tentatives = tentatives - 1
    print("-> Nope\n")
    if tentatives==0:
        print(" ==========Y= ")
    if tentatives<=1:
        print(" ||/       |  ")
    if tentatives<=2:
        print(" ||        0  ")
    if tentatives<=3:
        print(" ||       /|\ ")
    if tentatives<=4:
        print(" ||       /|  ")
    if tentatives<=5:                    
        print("/||           ")
    if tentatives<=6:
        print("==============\n")

#la on affiche le nombre de lettres qu'il va falloir deviner en mettant des _ popur chaque lettre
  affichage = ""
  for x in mot:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

#La on définit que si il n'y a plus de _ la partie se finit
  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break
     
print("\n Fin de partie    ")
# \n sert de retour à la ligne