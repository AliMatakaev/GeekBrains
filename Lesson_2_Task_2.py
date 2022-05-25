lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

def get_sign(x):
    if x[0] in '+-':
        return x[0]

i = 0
while i < len(lst):
    sign = get_sign(lst[i])
    if lst[i].isdigit() or (sign and lst[i][1:].isdigit()):
        if sign:
            lst[i] = sign + lst[i][1:].zfill(2)
        else:
            lst[i] = lst[i].zfill(2)

        lst.insert(i, '"')
        lst.insert(i + 2, '"')
        i += 2

    i += 1

print(" ".join(lst))