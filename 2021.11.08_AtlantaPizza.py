#AtlantaPizza.py - простой калькулятор стоимости пиццы
number_of_pizzas = eval(input("Сколько пицц вы хотите? "))
#Запросить стоимость пиццы по меню
cost_per_pizza = eval(input("Сколько стоит пицца? "))

#Подсчитать общую стоимость пиццы как подытог
subtotal = number_of_pizzas * cost_per_pizza

#Подсчитать сумму налога с продаж по ставке 8% от подытога
tax_rate = 0.08
sales_tax = subtotal * tax_rate

#Приплюсовать налог с продаж к подытогу для подсчета итога
total = subtotal + sales_tax

#Показать пользователю общую сумму к оплате,
#в том числе налог
print("Полная стоимость $", total)
print("В том числе $", subtotal, " за пиццу и")
print("$", sales_tax, "налог с продаж")
