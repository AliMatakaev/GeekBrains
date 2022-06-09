src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
used = []
i = 0
while i < len(src):
    if src[i] in src[i+1:]:
        used.append(src[i])
    elif src[i] not in used:
        result.append(src[i])
    i+=1
print(result)