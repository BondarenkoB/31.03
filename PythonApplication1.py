def unique_elements(nums):
    unique_nums = [12312412421]
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums
