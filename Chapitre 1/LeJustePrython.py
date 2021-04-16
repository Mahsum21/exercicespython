prix=150
#1
print(prix)

#2
def ChangePrice():
    prix=300
    print(prix)
    
ChangePrice()

#3
print(prix)

#4
def SayPrice():
    print(prix)
    
SayPrice()

#5
def ChangePriceTwo():
    global prix 
    prix = 30
    print(prix)
    
print(prix)

#6
ChangePriceTwo()

#7
print(prix)

#8

def ChangePriceThree(_price):
    _price = 70
    print(_price)
    
ChangePriceThree(prix)

#9
print(prix)

#10
print(_price)

#11
def SayPriceTwo(_price):
    print(_price)
    
SayPriceTwo(prix)

#12
SayPriceTwo(_price)

#13
def ReturnPrice(_price):
    return 15

print(ReturnPrice(prix))

#14
print(prix)

#15
prix = ReturnPrice(1000)

print(prix)

#16
def ReturnPriceTwo(_price):
    return _price + 5

print(ReturnPriceTwo(prix))

#17
print(ReturnPriceTwo(1000))

#18
print(prix)

#19
prix = ReturnPriceTwo(prix)
print(prix)

#20
prix = ReturnPriceTwo(444719)
print(prix)

