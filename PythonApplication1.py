import random
random_list = [random.randint(-10, 10) for i in range(10)]

even_numbers = []
odd_numbers = []
negative_numbers = []
positive_numbers = []
#func
for number in random_list:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
    if number < 0:
        negative_numbers.append(number)
    elif number > 0:
        positive_numbers.append(number)


print("Випадковий список:", random_list)
print("Парні числа:", even_numbers)
print("Непарні числа:", odd_numbers)
print("Від'ємні числа:", negative_numbers)
print("Додатні числа:", positive_numbers)
