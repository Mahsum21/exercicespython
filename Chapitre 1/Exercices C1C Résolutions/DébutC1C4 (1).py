import sys
def ChooseDestination():
    print("1 - Bruxelles\n2 - Mons\n3 - Nivelles \n4 - Charleroi")
    _destinationChoice = int(input("Entrez La destination que vous voulez atteindre :\n "))

    if _destinationChoice == 1:
        _destination = "Bruxelles"

    elif _destinationChoice == 2:
        _destination = "Mons"

    elif _destinationChoice == 3:
        _destination = "Nivelles"

    elif _destinationChoice == 4:
        _destination = "Charleroi"
    else :
        sys.exit("Erreur : la destination entrée est incorrecte !")

    print("Bien, vous avez choisi d'aller à " + _destination +".\n")
    return _destination

def ChoosePeriodOfTime():
    print("1 - Matin\n2 - Après-midi\n3 - Soir")  
    _timeChoice = int(input("Quand souhaitez vous partir ? "))

    if _timeChoice == 1:
        _time = "Matin"
    elif _timeChoice == 2:
        _time = "Après-midi"
    elif _timeChoice == 3:
        _time = "Soir"
    else :
        sys.exit("Erreur : période entrée n'est pas correcte !")

    print("Ok, vous avez choisi la période : " + _time + "\n")
    return _time