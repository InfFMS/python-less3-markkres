# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".
def Is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a=[]
N=int(input())
for i in range(N):
    b=int(input())
    if Is_prime(b):
        a.append(b)
if a==[]:
    print("no")
else:
    print(min(a),max(a))

