import random


print('Welcome to the "Guess the Number" Game')

print("The number is between 1 to 100")

number = random.randint(1,100)

guess = 0

def sicakSoguk():
    diff = abs(number-guess)
    if (0 < diff <= 5):
        print("Your on fire!!!")    
    elif (5 < diff <= 10):
        print("Tooooo hot!")
    elif (10 < diff <= 20):
        print("Warm enough")
    elif (20 < diff <= 30):
        print("Mid")
    elif (30 < diff <= 50):
        print("You're getting colder")        
    elif (number == guess):
        print("Congratulations!")
    else:
        print("You're really cold")


numbers = ["", "st", "nd", "rd"]

i=1


while guess!=number:

    if i < 4:
        newNum = str(i) + numbers[i]
    else:
        newNum = str(i) + "th"
    
    guess = int(input(f"Your {newNum} guess is: "))
    sicakSoguk()
    i+=1



