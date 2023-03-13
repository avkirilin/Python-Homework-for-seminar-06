# Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
lenght_list = random.randint(30, 47)
word = ''
if lenght_list % 10 == 0 or 4 < lenght_list % 10 < 10:
    word = 'элементов'
elif lenght_list % 10 == 1:
    word = 'элемент'
elif 1 < lenght_list % 10 < 5:
    word = 'элемента'
print(f"Длина списка: {lenght_list} {word}")
list = [random.randint(10, 30) for _ in range(lenght_list)]
print(f"Cписок значений: {list}")
min_num = random.randint(10, 20)
max_num = random.randint(20, 30)
print(f"Ищем значения в промежутке: {min_num} - {max_num}")
new_list = []
for i in range(len(list)):
    if min_num <= list[i] <= max_num:
        new_list.append(i + 1)
print(f"Номера элементов, лежащих в заданном промежутке: {new_list}")