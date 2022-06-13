
def hobbys():
    users = []
    hobbys = []
    result = {}

    with open('users.csv', 'r', encoding='utf-8') as persons:
        for line in persons:
            value = line.replace('\n', '').split(", ")
            users.append(value)

    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        for line in hobby:
            value = line.replace('\n', '').split(", ")
            hobbys.append(value)


    i = 0
    while i < len(users):
        if i < len(hobbys):
            result[str(users[i])]=hobbys[i]
        else:
            result[str(users[i])] = None
        i+=1
    print(result)

hobbys()

