nums = input("Введіть числа через пробіл: ").split()
nums = [int(num) for num in nums]

average = sum(nums) / len(nums)

count = 0
for num in nums:
    if num > average:
        count += 1

print("Кількість чисел, більших за середнє арифметичне:", count)

