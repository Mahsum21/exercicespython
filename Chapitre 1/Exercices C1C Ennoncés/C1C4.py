# Enoncé : Vous créez une petie application qui donne les horaires des trains. L'utilisateur choisira sa destination et la période à laquelle il veut partir et votre application
# donnera l'heure du train. Concrètement le résultat devra ressembler à ceci :

# 1 - Bruxelles
# 2 - Mons
# 3 - Nivelles
# 4 - Charleroi
# Entrez La destination que vous voulez atteindre : 3
# Bien, vous avez choisi d'aller à Nivelles.
# 1 - Matin
# 2 - Après-midi
# 3 - Soir
# Quand souhaitez vous partir ? 3
# Ok, vous avez choisi la période : Soir
# Votre train démarre à 20h00

# Les heures sont les suivantes :
# Bruxelles (Matin) : 10h33
# Bruxelles (Midi) : 14h42
# Bruxelles (Soir) : 19h02

# Mons (Matin) : 9h10
# Mons (Midi) : 13h30
# Mons (Soir) : 22h56

# Nivelles (Matin) : 5h34
# Nivelles (Midi) : 15h13
# Nivelles (Soir) : 20h00

# Charleroi (Matin) : 7h45
# Charleroi (Midi) : 12h53
# Charleroi  (Soir) : 23h02


import sys
def choosedestination():
    print("1 - bruéessel/n 2 - monse /N 3 - nivel /n 4 - charleroi ")
    _destinationchoice=int(input("entrez la destination que vous voulez attindre: "))
    if(_destinationchoice==1):
        _destination="bruxel"
    elif(_destinationchoice==2):
        _destination="monse"
    elif(_destinationchoice==3):
        _destination="nivel"
    elif(_destinationchoice==4):
        _destination="charleroi"
    else:
        sys.exit("erreur la destination entrez n'est pas correcte ")
    print("vous avez desidé d'aller à: " + _destination)
    return _destination
def chooseperiodoftime():
    print("1 - matin /n 2 - après-midi, 3 - soir ")
    _timechoice=int(input("quant voullez vous partir ? "))
    if(_timechoice==1):
        _time="matin"
    elif(_timechoice==2):
        _time="après-Midi"
    elif(_timechoice==3):
        _time="soir"
    else:
        sys.exit("la periode entrez n'est pas corecte")
    print("vous avez choisi la periode: " + _time)
    return _time

def displayTime(_time,_morninghour,_afternoonhour,_eveninhour):
    if _time=="matin":
        print("votre train démare à" + _morninghour)
    elif _time=="aprèsMidi":
        print("votre train démare à: " + _afternoonhour)
    elif -time=="soir":
        print("votre train démare à: " + _eveninhour)
        
    

destination=choosedestination()
time=chooseperiodoftime()

if destination=="bruxel":
    displayTime(time,"10h33","14h42","19h02")
elif destination=="monse":
    displayTime(time, "9h10", "15h30", "20h03")
elif destination=="nivel":
    displayTime(time,"11h00", "16h11", "21h11")
elif destination=="charleroi":
    displayTime(time,"0811", "13h11", "22h11")

    
    
    