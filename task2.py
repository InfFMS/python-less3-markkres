# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.
a=0
b=0
while True:
    vod=float(input())
    if vod==0:
        break
    elif vod==int(vod) and vod>0 and len(str(int(vod)))==2:
        a+=1
    else:
        b+=1
print(a,b)
