#fizzbuzz

# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

#おつり問題

# insert=input("insert:") #投入金
# product=input("product:") #商品の金額
# change =int(insert)-int(product) #おつり

# print(change)

# coin=[5000,1000,500,100,50,10,5,1]

# for i in coin:
#     r=change//i
#     change %=i
#     print(change)
#     print(str(i)+":"+str(r))

#十進数→二進数変換
# n=18

# result=""

# while n>0:
    
#     result=str(n%2)+result
#     n//=2

# print(result)

#二進数→十進数

# n="10010"

# result=0

# for i in range(len(n)):
#     result +=int(n[i])*(2**(len(n)-i-1))
    
# print(result)

#素数判定

import math

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):#平方根
        if n%i==0:
            return False
    return True

for i in range(200):
    if is_prime(i):
        print(i,end=" ")