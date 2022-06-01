def thesaurus(*names):
    name_dict = {}
    for name in names:
        key = name[0].capitalize()
        if key not in name_dict:
            name_dict[key] = []
        name_dict[key].append(name)
    print(name_dict)


thesaurus("Артур", "Сергей", 'Николай', 'Светлана', 'Наталья')