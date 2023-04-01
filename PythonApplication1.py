import random

n = int(input("Введіть кількість елементів списку: "))
nums = [random.randint(1, 100) for _ in range(n)]

even_count = 0
odd_count = 0

for num in nums:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Кількість парних чисел:", even_count)
print("Кількість непарних чисел:", odd_count)
