nums = input("Введіть числа через пробіл: ").split()
nums = [int(num) for num in nums]

positive_nums = []
for num in nums:
    if num > 0:
        positive_nums.append(num)

print("Додатні числа у списку:", positive_nums)

