#ユークリッドの互除法

#再帰関数を使わない
# print("a>=bとなる自然数を入力してください")

# a=int(input("a="))
# b=int(input("b="))

# while True:
#     r=a%b
#     if r==0:
#         print("それらの最大公約数は",b,"です")
#         break
#     a=b
#     b=r
    
def euclid(a,b):
    if b==0:
        return a
    else:
        return euclid(b,a%b)

print("a>=bとなる自然数を入力してください")

a=int(input("a="))
b=int(input("b="))
print("それらの最大公約数は",euclid(a,b),"です")