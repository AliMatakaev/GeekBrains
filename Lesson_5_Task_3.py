tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']

klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

i = 0

while i < len(tutors):
    if i < len(klasses):
        result = [tutors[i], klasses[i]]
    else:
        result = [tutors[i], None]
    print(tuple(result))
    i+=1