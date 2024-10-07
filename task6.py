# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
a=[]
while True:
    b=int(input())
    if b==0:
          break
    else:
        a.append(b)
if a==[]:
    print("")
else:
    print(min(a), max(a))
