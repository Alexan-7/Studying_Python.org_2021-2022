# сравним, какие слова встречаются в обоих текстах

r = open('2022.03.17_Text1.txt', encoding = 'UTF-8')
r1 = set(r.read().split()) # список превратили во множество без повторяющихся слов
r.close()

r = open('2022.03.17_Text2.txt', encoding = 'UTF-8')
r2 = set(r.read().split()) # список превратили во множество без повторяющихся слов
r.close()


# new = r1.difference(r2) # разница двух множеств (переменные, которыми множества отличаются: есть в r1, но нет в r2)
new = r2.difference(r1) # разница двух множеств (переменные, которыми множества отличаются: есть в r2, но нет в r1)
print(new) # во множестве new только уникальные слова из обоих текстов

input('Нажмите Enter для выхода')
