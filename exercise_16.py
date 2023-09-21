import random

user_size = int(input('Введите количество элементов массива: '))

numbers = [random.randint(-10,10) for _ in range(user_size)]
print(*numbers)

user_num = int(input('Введите число для поиска: '))
count = 0

for i in range(len(numbers)):
    if user_num == numbers[i]:
        count += 1

print(count)
