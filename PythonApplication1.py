# -*- coding: cp1251 -*- 
import random
number = []
for i in range(0,19):
    number.append(random.randint(-40, 40))
print(number)

negat_sum = 0
par_sum = 0
nepar_sum = 0
krante3_dob = 1
product_between_min_max = 1

#1 func
for num in number:
    if num < 0:
        negat_sum += num
print('Сума від’ємних чисел:', negat_sum)

#2 func
for num in number:
    if num % 2 == 0:
        par_sum += num
print('Сума парних чисел:', par_sum)

#3 func
for num in number:
    if num % 2 != 0:
        nepar_sum += num
print('Сума непарних чисел:', nepar_sum)

#4 func
for num in range(len(number)):
    if num % 3 == 0:
        krante3_dob *= number[num]
print('Добуток елементів з індексами, кратними 3:', krante3_dob)

#5 func
min_index = number.index(min(number))
max_index = number.index(max(number))

if min_index > max_index:
    min_index, max_index = max_index, min_index

for num in number[min_index+1:max_index]:
    product_between_min_max *= num
print("Добуток елементів між мінімальним та максимальним елементом:", product_between_min_max)

#6 func
pos_indexes = [num for num in range(len(number)) if number[num] > 0]
if len(pos_indexes) > 1:
    first_pos_index = pos_indexes[0]
    last_pos_index = pos_indexes[-1]
    sum_between_pos = sum(number[first_pos_index+1:last_pos_index])
    print("Сума елементів, що знаходяться між першим та останнім додатним елементом:", sum_between_pos)
else:
    print("В масиві немає двох додатніх елементів.")

