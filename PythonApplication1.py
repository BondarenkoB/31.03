words = input("Введіть слова через пробіл: ").split()

words.sort(key=len)

print("Слова відсортовані за зростанням довжини:")
print(words)
