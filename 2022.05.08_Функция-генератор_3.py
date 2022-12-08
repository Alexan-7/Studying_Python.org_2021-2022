def some():
    with open('2022.05.06_Text.txt', encoding='utf-8') as r:
        for x in r:
            yield x

p = some()

print(p)
