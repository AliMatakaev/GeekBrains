def get_jokes(n):
    """
    get_jokes(n)
    Gives jokes formed from three random words taken from three lists. The attribute specifies the number of jokes.
    """
    from random import randint
    result = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    advebs = ["сегодня", "вчера", "завтра", "позавчера","ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 1
    while i <= n:
        result.append(nouns[randint(0,4)] + ' ' + advebs[randint(0, 4)] + ' ' + adjectives[randint(0, 4)])
        i += 1
    print(result)

get_jokes(5)