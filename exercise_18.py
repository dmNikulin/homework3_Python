import random
import math

user_size = int(input('Введите количество элементов массива: '))
numbers = [random.randint(0,5) for _ in range(user_size)]
print(numbers)

user_num = int(input('Введите число для поиска: '))
list_numbers = []
diff_1 = 0                                           # Переменная будет искать разницу введеного числа и числа в списке

for i in range(len(numbers)):                       
    if numbers[i] == user_num:                       # Если находим совпадение, то стоп
        print(user_num)
        break
    else:                                            #Если нет, то записываем разности по модулю в список
        diff_1 = user_num - numbers[i]
        list_numbers.append(abs(diff_1))
    
print(list_numbers)

find_min = list_numbers[0]
list_index =[]

for j in range(len(list_numbers)):                  #Находим наименьшую разность
    if list_numbers[j] < find_min:
        find_min = list_numbers[j]

for k in range(len(list_numbers)):                  # Записываем индекс с наименьшей разностью
    if find_min == list_numbers[k]:
        list_index.append(k)

print(list_index)

for t in range(len(list_index)):                    # Выводим
    print(f'Вашего числа нет в списке, самое близкое к нему: {numbers[list_index[t]]}')
