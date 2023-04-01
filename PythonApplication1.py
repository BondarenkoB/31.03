nums = input("Введіть числа через пробіл: ").split()
nums = [int(num) for num in nums]

squares = []
for num in nums:
    squares.append(num**2)

print("Квадрати чисел у списку:", squares)

