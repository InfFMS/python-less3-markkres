# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.
import math
suma=0
col=0
while True:
    a=int(input())
    if a==0:
        break
    elif math.log2(a)==int(math.log2(a)):
        suma+=a
        col+=1
if col==0:
    print("no")
else:
    print(suma/col)
