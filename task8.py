# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить, сколько было введено положительных и
# сколько отрицательных чисел (нули не считать!).
N=int(input())
pos=0
neg=0
for i in range(N):
    a=int(input())
    if a>0:
        pos+=1
    elif a<0:
        neg+=1
print(pos,neg)
