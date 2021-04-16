print("Vous vous appretez à rentrer sur un site de chatons beaucoup trop mignon, si vous avez plus de 18 ans, vous n'êtes plus assez pur pour rentrer sur ce site")
userInput = input("Si vous avez plus de 18 ans ecrivez ecrivez la phrase se trouvant dans les guillemets suivants :\n\"les chatons sont trop mignons pour moi\"\n")

if userInput == "les chatons sont trop mignons pour moi" :
    print("Vous avez plus de 18 ans, nous vous redirigeons hors du site.")
else :
    print("bienvenue sur ce site chatongraphique.")

# Meilleure solution :

adultSentence = "les chatons sont trop mignons pour moi"
print("Vous vous appretez à rentrer sur un site de chatons beaucoup trop mignon, si vous avez plus de 18 ans, vous n'êtes plus assez pur pour rentrer sur ce site")
userInput = input("Si vous avez plus de 18 ans ecrivez ecrivez la phrase se trouvant dans les guillemets suivants : \n\"" + adultSentence + "\" \n")

if userInput == adultSentence :
    print("Vous avez plus de 18 ans, nous vous redirigeons hors du site.")
else :
    print("bienvenue sur ce site chatongraphique.")