persons = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
i = 0
temp_list = ['0']
while i < len(persons):
    temp_list[0] = persons[i]
    new_list = [word for line in temp_list for word in line.split()]
    n = len(new_list)-1
    print('Привет,', new_list[n].title()+'!')
    i+=1