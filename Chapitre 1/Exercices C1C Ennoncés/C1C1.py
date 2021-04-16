# Enoncé : Votre programme demandera la donnée "heure" de l'heure à l'utilisateur et stockera la réponse dans une variable
# Ensuite, il demandera la donnée "minute" de l'heure à l'utilisateur et stockera cette deuxième information dans une autre variable.
# Après recolte de ces informations, le programme écrira l'heure que l'utilisateur a défini. Si l'heure n'est pas correctement encodée 
# (minutes supérieur à 59, heures supérieures à 24,...) alors le programme affichera en plus un message d'erreur du style pour faire comprendre le problème.
# Après ceci, quoi qu'il arrive, le programme souhaitera une bonne journée à l'utilisateur.

#region indice
# pour créer une condition on utilise le petit mot if suivi de la condition à respecter entre parenthèse suivi du signe deux points. A la ligne, avec une tabulation,
# on écrit ce que fait le programme si la condition est respectée.
#endregion

#region indice
# exemple de condition :
# if(condition):
#   JeFaisCeci()
#endregion

#region indice
# Une condition est une expression booléenne, le résultat ne peut être que true ou false, souvenez vous des cours théorique ! (>,<,>=,<=,==,or,and,not)
#endregion

#region indice
# Réflechissez au placement de chacune de vos actions, quelles sont les conditions pour qu'elles se déclanchent, si il faut en respecter une ou pas, et en fonction, placer votre
# action au bon endroit dans le code, attention à l'indentation !!! (tabulations)
#endregion

heure=int(input("quel heure est-il ?"))    
minute=int(input("quel minute est-il ?"))
print("il est: " + str(heure) + "h " +str(minute))

if(heure<0):
    print("vous ne pouvez pas entrer un nombre inférieur à 0: " + str(heure))
    
if(minute<0):
    print("vous ne pouvez pas entrer un nombre inférieur à 0: " + str(minute))
    
if(heure>23):
    print("vous ne pouvez pas entrer un nombre supérieur à 23: " + str(heure))
    
if(minute>59):
    print("vous ne pouvez pas entrer un nombre supérieur à 59: " + str(minute))
print("bonne journée")