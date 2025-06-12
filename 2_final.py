import re

NumberDict = {'1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять', '0': 'ноль'}

ReadNumbers = []
NumberSum = 0
NumberMax = 0
CurrentMax = 0


with open('1_test.txt', 'r') as file:
    for line in file:
        CheckNumbers = re.findall(r'\b[0-9a-fA-F]+\b', line)
        for Number in CheckNumbers:
            if len(Number) > 1:
                Number = int(Number, 16)
                if (Number % 2 == 0) and (Number <= 2048):
                    ReadNumbers.append(Number)

NumberSum += len(ReadNumbers)
NumberMax = max(ReadNumbers)

Words = []
NumberMaxStr = str(NumberMax)
for i in NumberMaxStr:
    Words.append(NumberDict[i])

print(ReadNumbers)
print("Количество чисел: ", NumberSum)
print("Максимальное число: \n", NumberMax)
print(' '.join(Words))
