numbers = list(range(1, 1000, 2))

cubic_numbers = []
i = 0
while i < len(numbers):
    cubic_numbers.append(numbers[i] ** 3)
    i += 1

sum_numbers_1 = []
i = 0
while i < len(cubic_numbers):
    sum_numbers_1.append(sum(map(int, str(cubic_numbers[i]))))
    i += 1

multiples_1 = []
i = 0
while i < len(sum_numbers_1):
    if sum_numbers_1[i] % 7 == 0:
        multiples_1.append(sum_numbers_1[i])
    i += 1
print('Первый ответ: ',sum(multiples_1))

added_numbers = []
i = 0
while i < len(cubic_numbers):
    added_numbers.append(cubic_numbers[i] + 17)
    i += 1

sum_numbers_2 = []
i = 0
while i < len(added_numbers):
    sum_numbers_2.append(sum(map(int, str(added_numbers[i]))))
    i += 1

multiples_2 = []
i = 0
while i < len(sum_numbers_2):
    if sum_numbers_2[i] % 7 == 0:
        multiples_2.append(sum_numbers_2[i])
    i += 1
print('Второй ответ: ',sum(multiples_2))