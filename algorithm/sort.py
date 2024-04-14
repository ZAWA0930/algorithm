#=====選択ソート=====
#データの並びから最も小さな値を探し、その先頭のでデータと入れ替えます。
#降順や昇順に並べる手法

# data=[9,3,7,1,4,2,5,8,6,0]
# print(data,"元のデータ")

# for i in range(0,9):#0~8まで増える
#     m=i #最小値の値
#     print(m)
#     for j in range(i+1,10): #i+1から9まで1づつ増える
#         if data[j]<data[m]:  #data[j]がdata[m]より小さければ
#             m=j
            
#     data[i],data[m]=data[m],data[i]
#     print(data,i+1)#過程を出力

# print(data,"ソート後のデータ")

#=====バブルソート=====

# data=[9,3,7,1,4,2,5,8,6,0]
# print(data,"元のデータ")
# n=len(data)

# for i in range(0,n-1):
#     for j in range(n-1,i,-1):
#         if data[j-1]>data[j]:
#             data[j],data[j-1]=data[j-1],data[j]

# print(data,"ソート後のデータ")

#=====挿入ソート=====


# data=[9,3,7,1,4,2,5,8,6,0]
# print(data,"元のデータ")
# n=len(data)

# for i in range(1,n):
#     tmp=data[i]
#     j=i
#     while j>0 and data[j-1]>tmp:
#         data[j]=data[j-1]
#         j=j-1
#     data[j]=tmp

# print(data,"ソート後のデータ")


#並べるデータをランダムで作り出す

# import random
# n=15
# data=[0]*n
# for i in range(n):
#     data[i]=random.randint(1,99)
# print(data,"元データ")


# for i in range(1,n):
#     tmp=data[i]
#     j=i
#     while j>0 and data[j-1]>tmp:
#         data[j]=data[j-1]
#         j=j-1
#     data[j]=tmp

# print(data,"ソート後のデータ")


#=====クイックソート=====

# import random
# n=15
# data=[0]*n
# for i in range(n):
#     data[i]=random.randint(1,99)
# print(data,"元データ")

# def quick_sort(left,right):
#     i=left
#     j=right
#     p=data[(left+right)//2]
#     while True:
#         while data[i]<p:
#             i=i+1
#         while data[j]>p:
#             j=j-1
#         if i>=j:
#             break
#         data[i],data[j]=data[j],data[i]
#         i=i+1
#         j=j-1
#     if left < i-1:
#         quick_sort(left,i-1)
#     if right >j+1:
#         quick_sort(j+1,right)


# quick_sort(0,n-1)
# print(data,"ソート後のデータ")


#=====マージデータ=====
#マージとはデータを一つにまとめること

# a=[1,3,4,7,8,9]
# b=[0,2,5,6]
# na=len(a)
# nb=len(b)


# c=[0]*(na+nb)

# i=0
# j=0
# p=0

# print(a,"データA")
# print(b,"データB")

# while i <na and j<nb:
#     if a[i] <= b[j]:
#         c[p]=a[i]
#         i+=1
#         p+=1
#     else:
#         c[p]=b[j]
#         j+=1
#         p+=1

# while i<na:
#     c[p]=a[i]
#     i+=1
#     p+=1

# while j<nb:
#     c[p]=b[j]
#     j+=1
#     p+=1

# print(c,"マージ後のデータ")
                

#=====ヒープソート=====

data=[1,2,4,5,3,6,8]
n=len(data)

print(data,"元のデータ")

for i in range((n-1)//2,-1,-1):
    p=i
    c=p*2+1
    while c<n:
        if c<n-1 and data[c]<data[c+1]:
            c+=1
        if data[p] >=data[c]:
            break
        data[p],data[c]=data[c],data[p]
        p=c
        c=p*2+1

print(data,"初期ヒープ")
    