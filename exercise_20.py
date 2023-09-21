letter = input('Введите слово: ')

def isEnglish(letter): # состоит ли строка из английских букв
    return letter.isascii() and letter.isalpha()


score_base_ru = {'А': 1, 'В': 1,'Е': 1, 'И': 1,'Н': 1, 'О': 1,'Р': 1, 'С': 1,'Т': 1,
              'Д': 2, 'К': 2,'Л': 2,'М': 2,'П': 2, 'У': 2,
              'Б': 3,'Г': 3, 'Ё': 3,'Ь': 3, 'Я': 3,
              'Й': 3,'Ы': 3,
              'Ж': 4,'З': 4, 'Х': 4,'Ц': 4, 'Ч': 4,
              'Ш': 8,'Э': 8, 'Ю': 8,
              'Ф': 10,'Щ': 10, 'Ъ': 10}

score_base_en = {'A': 1, 'E': 1,'I': 1, 'O': 1,'U': 1, 'L': 1,'N': 1, 'S': 1,'T': 1,'R': 1,
              'D': 2, 'G': 2,
              'B': 3,'C': 3, 'M': 3,'P': 3,
              'F': 4,'H': 4, 'V': 4,'W': 4, 'Y': 4,
              'K': 5,
              'J': 8,'X': 8,
              'Q': 10,'Z': 10}

count = 0
letter = letter.upper()

if letter.isascii() and letter.isalpha():
    for i in range(len(letter)):
        count += score_base_en.get(letter[i])

else:
    for i in range(len(letter)):
        count += score_base_ru.get(letter[i])

print(count)

