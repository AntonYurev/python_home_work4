# Вычислить число c заданной точностью d (10^{-1} ≤ d ≤10^{-10})
# import random
# n = random.random()*(random.randint(1, 20))
# print ('Наше число: ', n)
# d = str(input('Введите точность округления: '))
# d = d.split('.')
# print ('Вычисленное число: ', round(n, len(d[1])))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
# n = int(input('Введите натуральное число: '))
# a = []
# i = 2
# while n != 1 :
#     if n % i == 0:
#         a.append(i)
#         n = n//i
#         i = 1
#     i = i +1
# if len(a) == 1:
#     print('Число простое')
# else:
#     print ('Простые множители числа: ', a)

# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# import random
# def f(x):
#     return random.randint(1,15)

# a = [f(i) for i in range(20)]
# print('Наша последовательность чисел: ', a)
# i = 0
# j = 1
# while i != len(a):
#     while j != len(a):
#         if a[i] == a[j]:
#             del a[j]
#             j -=1
#         j +=1
#     i +=1
#     j = i+1
# print('Новый список: ', a)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# import random
# k = int(input('Введите степень многочлена: '))
# def f(x):
#     return random.randint(0,100)

# a = [f(i) for i in range(k+1)]
# s = ''
# for i in range (k-1):
#     if a[i] != 0:
#         s = s + str(a[i]) + 'x**' + str(k-i) + ' + '
# if a[k-1] == 0 and a[k] == 0:
#     s = s + ' = 0'
# elif a[k-1] == 0 and a[k] !=0:
#     s = s + str(a[k]) + ' =0'
# elif a[k-1] !=0 and a[k] == 0:
#     s = s + str(a[k-1]) + 'x ' + ' = 0'
# else :
#     s = s + str(a[k-1]) + 'x ' + '+ ' + str(a[k]) + ' = 0'  
# f1 = open('newfile.txt', 'w')
# f1.write(s)
# f1.close()


    




