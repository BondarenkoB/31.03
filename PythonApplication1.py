nums = input("Введіть числа через пробіл: ").split()
nums = [int(num) for num in nums]

min_index = nums.index(min(nums))
max_index = nums.index(max(nums))

nums[min_index], nums[max_index] = nums[max_index], nums[min_index]

print("Список зі зміненими місцями мінімального та максимального елементів:")
print(nums)

