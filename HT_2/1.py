# Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
# Елементами списку повинні бути як рядки, так і числа.

test_list = [1, 2, 'test', 10, 'foo']
summ = "".join(map(str, test_list))

print(summ)