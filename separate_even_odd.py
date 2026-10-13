numbers = [10, 15, 20, 25, 30, 35]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Original list:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
