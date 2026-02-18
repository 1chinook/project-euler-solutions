record_lenght = 0
record_number = 0

def chainFinder(sayi):
    sayac = 1
    while sayi != 1:
        if sayi % 2 == 0:
            sayi = sayi // 2
        else:
            sayi = (sayi * 3)+1
        sayac+=1
    return sayac
   
for number in range(2,1000000):
    lenght = chainFinder(number)
    if lenght > record_lenght:
            record_lenght = lenght
            record_number = number


print(f"{record_number} and {record_lenght}")
