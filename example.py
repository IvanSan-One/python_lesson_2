# Задачи на циклы и оператор условия------
#----------------------------------------

'''

#Задача 1
#Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# for i in range(5):print(i,0)
'''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# num = 0
# for i in range(10):
#     e = input('введите цифру')
#     if int(e)==5:num +=1
# print('Найдено цифр 5:',num,'штук')

'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
# for i in range(1,101):
#     sum+=i
#     print(sum) # визаулизация (не обязательно)
# print(sum)
'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# com = 1
# for i in range(1,11):
#     com*=i
#     print(com) # визаулизация (не обязательно)
# print(com)
'''
Задача 5

Вывести цифры числа на каждой строчке.
'''
# #integer_number = 2129
# #print(integer_number%10,integer_number//10)

# integer_number = int(input('введите число'))
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6

Найти сумму цифр числа.
'''
# e=int(input('Введите число:'))
# sum=0
# while e>0:
#     sum +=e%10
#     e=e//10
# #    print(sum)                       На посмотреть!
# print('Сумма цифр равна:',sum)

'''
Задача 7

Найти произведение цифр числа.
'''
# e=int(input('Введите число:'))
# com=1
# while e>0:
#     com *=e%10
#     e=e//10
# #    print(com)                      На посмотреть!
# print('Произведение цифр равна:',com)
'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = int(input('Введите число:'))
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Да, есть 5')
#         break
#     integer_number = integer_number//10
# else: print('Нету 5-ки')

'''
Задача 9

Найти максимальную цифру в числе
'''
# integer_number = int(input('Введите число:'))
# big=0
# while integer_number>0:
#     if integer_number%10>big:
#         big=integer_number%10
#     integer_number = integer_number//10
# print('В вашем числе самая большая цифра:',big)

'''
Задача 10.тест
Найти количество цифр 5 в числе
'''
integer_number = int(input('Введите число:'))
big=0
while integer_number>0:
    if integer_number%10 == 5:
        big +=1
    integer_number = integer_number//10
print('В вашем числе количество 5:',big)


