units = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["","", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens = ["ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen" ,"eighteen" ,"nineteen"]
numbers = []


def numTranslator(num):
    if num < 10:
        return units[num]
    

    elif 10 <= num < 20:
        newNum = int(num) - 10
        return teens[newNum]
    
    
    elif 20 <= num < 100:
        tensValue = num // 10
        unitsValue = num % 10
        if unitsValue == 0:
            return tens[tensValue]
        else:
            return tens[tensValue] +  units[unitsValue]
        

    elif 100 <= num < 1000:
        tensValue = (num % 100) // 10 
        unitsValue = num % 10
        hundredsValue = num // 100
        if unitsValue == 0 and tensValue == 0:
            return units[hundredsValue] + "hundred"
        elif tensValue == 0:
            return units[hundredsValue] + "hundredand" + units[unitsValue]
        elif 10 <= num % 100 < 20:
            return units[hundredsValue] + "hundredand" + teens[unitsValue]
        else:
            return units[hundredsValue] + "hundredand" + tens[tensValue] + units[unitsValue]

for number in range(1,1000):
    translated = numTranslator(number)
    numbers.append(translated)


toplam = 0
for word in numbers:
    toplam += len(word)

print(toplam + 11) # we should add one thousand but unnecesarry for another code block. Lenght of 'onethousand' is 11




            