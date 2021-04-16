hour = int(input("Quelle heure est-il ?"))
minutes = int(input("Il est " + str(hour) + " heure, mais combien de minutes ?"))

print("Ok il est " + str(hour) + "h" + str(minutes))

if hour > 24:
    print("L'heure entrée est supérieure à 24")
    
if hour < 0:
    print ("L'heure entrée est inférieure à 0")
    
if minutes > 60:
    print ("Les minutes entrées sont supérieure à 60")

if minutes < 0:
    print("Les minutes entrées sont inférieure à 0")
    
print("Au revoir")