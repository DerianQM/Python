__author__ = 'Гущин Дмитрий Валерьевич'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

a = float('inf')
"""""
    Решение честно загуглено, тк этих свойст Float я не знал
    my_float = float('nan')  # nan — «не число» (NaN — not-a-number)
    my_float = float('inf')  # inf — бесконечность
    my_float = float('+inf')  # inf — бесконечность
    my_float = float('-inf')  # -inf — минус бесконечность
"""

print("a == a**2 - ",a == a**2) #True
print("a == a*2 -",a == a*2) #True
print("a > 999999", a > 999999) #True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)