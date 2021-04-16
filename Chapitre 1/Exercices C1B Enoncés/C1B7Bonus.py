# Enoncé : Ecrivez un programme qui fera office de super calculette ! Le programme demande de rentrer 2 
# chiffres à l'utilisateur, une fois ceux-ci entré, le programme donne le résultat de l'addition,
# la multiplication, la soustraction, la division et le résultat de chacun des nombres mis au carré.
# Chacune des opérations citées doivent se trouver dans une fonction différente.

#region indice
# On peut fonctionner de plusieurs manières pour résoudre cet exercice, essayon déjà de faire une fonction
# qui prend en paramètre 2 variables et qui renvoie le résultat de la somme de ces deux nombres
# Ensuite dans le programme principal on appelle cette fonction pour voir si elle fonctionne
#endregion

#region indice
# Si ça marche, on a juste à recréer 4 autres fonctions pour les 4 autres opérations
#endregion

#region indice
# Pour renvoyer un résultat, on met le petit mot return suivi du résultat. une fonction ne peut renvoyer 
# qu'une seule valeur, pour le carré il faut donc faire appel 2 fois à la même fonction !
#endregion

numberOne=int(input("entrez le premier chiffre: "))
numberTwo=int(input("entrez le deusième chiffre: "))
    
def Addition(_numberOne,_numberTwo):
    return _numberOne + _numberTwo

print("le résulta est: " + Addition(numberOne,numberTwo))


def Soustraction(_numberOne,_numberTwo):
    return _numberOne - _numberTwo

print("le résulta est, " + Soustraction(numberOne,numberTwo))


def Multiplication(_numberOne,_numberTwo):
    return _numberOne * _numberTwo

print("le résulta est, " + Multiplication(numberOne,numberTwo))

def Division(_numberOne,_numberTwo):
    return _numberOne / _numberTwo

print("le résulta est: " + Division(numberOne,numberTwo))
