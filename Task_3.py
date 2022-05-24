n = int(input('Введите проценты от 1 до 100: '))

words = ('процент', 'процента', 'процентов')

if (n % 10 == 0 or
    4 < n < 20 or
    4 < n % 10 < 10):
        print(n, words[2])
elif (1 < n < 5 or
    1 < n % 10 < 5):
        print(n, words[1])
elif (n == 1 or
    n % 10 == 1):
        print(n, words[0])