url1 = 'https:\www.youtube.com\new' # экранированный символ \n
url2 = 'https:\www.youtube.com\\new' # чтобы отображалось корректно, добавим \ к \

# os.walk('D:\\') # один слэш экранирует кавычку, поэтому дублируем его

url3 = r'https:\\www.youtube.com\new' # итерал r перед строкой

x = 'C:\\Users\\Default\\AppData' # указывать по ДВА слэша
a = r'C:\Users\Default\AppData' # ...или итерал r, чтобы не было ошибки
i = 'C:/Users/Default/AppData' # в Linux используется прямой слэш, поэтому проблем не возникает

print(url1)
print(url2)
print(url3)
print(x)
print(a)
print(i)
input('Нажмите Enter для выхода')
