# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.
def Is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

prime=0
ost=0
while True:
    a=int(input())
    if a==0:
        break
    elif Is_prime(a):
        prime+=1
    else:
        ost+=1
print(prime,ost)
