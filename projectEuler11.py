numbers = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"""


result = [[int(x) for x in line.split()] for line in numbers.splitlines()]
max_result = 0

for i in result:
    for j in i:
        first_result = j * j+1 * j+2 * j+3
        print(first_result)
        
    
