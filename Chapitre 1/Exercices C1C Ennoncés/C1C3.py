# Enoncé : Votre programme demande à l'utilisateur d'entrer un chiffre, ce chiffre représentera le sexe la personne (1:femme 2:homme 3:autre)
# En fonction de l'entrée donnée, le programme donnera un résultat différent, le programme saluera la personne en prenant en compte son sexe, 
# (Boujour Madame/Boujour Monsieur/Bonjour à vous)
#  Si la personne rentre une autre donnée, le programme dira à l'utilisateur que sont entrée est incorrecte.

#region indice
# Ce problème est resolvable de plusieurs manière. La plus instinctive est sans doutes une suite if, mais pour autant ce n'est pas la plus optimisée
#endregion

#region indice
# Il existe un troisième petit mot dans les conditions qui est elif. elif est un mot valise composé de else et de if, et qui veut litéralement dire "sinon si"
# essayez d'utiliser ceci pour gérer les conditions avec plus de 2 possibilités
#endregion

#region indice
# La syntaxe reste la même que jusque maintenant :
# if(condition1):
#   JeFaisAction1()
# elif(condition2):
#   JeFaisAction2()
# else:
# JeFaisActionparDefaut()
#endregion


print("pour déffinir votre sexe veillez entrer un chiffre entre 1 et 3")
sexe=int(input("entrez votre chiffre: "))
mise=1
mister=2
autre=3
if(sexe==mise):
    print("bonjour madame")
elif(sexe==mister):
    print("bonjour monsieur")
elif(sexe==autre):
    print("bonjour autre")
else:
    print("le caractère entrez ne corespond pas aux chois que nous vous avons donner. recomencez")