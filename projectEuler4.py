max_palindrome = 0

for i in range(999,99, -1):
    for j in range(999,99, -1):
        number = i * j
        str_number = str(number)
        if str_number == str_number[::-1]:
            if number > max_palindrome:
                max_palindrome = number

print(max_palindrome)
