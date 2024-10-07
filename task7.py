# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное из введённых чисел Фибоначчи.
# Вывести "нет", если чисел Фибоначчи в последовательности нет.
# Числа Фибоначчи – это последовательность чисел,
# которая начинается с двух единиц и каждое следующее число
# равно сумме двух предыдущих: 1, 1, 2, 3, 5, 8, 13, …
def F(n):
    a=[1,1]
    while a[-1]<=n:
        a.append(a[-1]+a[-2])
    return a
def is_in(n):
    a=F(n)
    for i in range(len(a)):
        if n==a[i]:
            return True
    return False
mas=[]
while True:
    vod=int(input())
    if vod==0:
        break
    elif is_in(vod):
        mas.append(vod)
if mas==[]:
    print("no")
else:
    print(min(mas))
