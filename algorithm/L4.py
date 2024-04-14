#=====線形探索=====

#線形探索はデータの先頭から1つずつ値を調べる

#forを使用
# data=[57,48,46,52,45,59,61,60,49,71]

# n=len(data)
# key=60
# flg=False
# for i in range(n):
#     if data[i]==key:
#         print("data[{}]が{}です".format(i,key))
#         flg=True
#         break

# if flg==False:
#     print(str(key)+"は存在しません")

#whileを使用
# data=[57,48,46,52,45,59,61,60,49,71]

# n=len(data)
# key=60

# i=0

# while i<n and data[i]!=key:
#     i+=1

# if i == n:
#     print(str(key)+"は存在しません")
# else:
#     print("data[{}]が{}です".format(i, key))

#入力した名前がデータに存在するとき、相手の電話番号を出力するもの

# data=[
#     ["佐藤","000-0000-0000"],
#     ["鈴木","111-1111-1111"],
#     ["高橋","222-2222-2222"],
#     ["田中","333-3333-3333"],
# ]

# n=len(data)
# s=input("検索する名前:")

# i =0

# while i<n and data[i][0]!=s:
#     i+=1
#     print(i)
    
# if i==n:
#     print("その名前は登録していません")
# else:
#     print(data[i][0]+"さんの番号は"+data[i][1]+"です")

#=====二分探索=====
# data=[1,2,9,12,20,25,32,48,50,57,72,78,80,93,100]

# key=int(input("探す値を入力してください:"))

# left=0
# right=len(data)-1

# flg=False

# while left <=right:
#     mid = (left+right)//2 #midにLeft,Rightの真ん中の値を代入
#     print("L={}  M={}  R={}".format(left,mid,right))
#     if data[mid]==key:
#         print("data[{}]が{}です".format(mid,key))
#         flg=True
#         break
#     if data[mid] < key:
#         left = mid+1  #data[mid]がkeyより小さいならleftにmid+1を代入
#     else:
#         right=mid-1   #data[mid]がkeyより大きいならrightにmid-1を代入

# if flg==False:
#     print("その値は存在しない")

#=====木探索=====

# #深さ優先探索
# #再帰関数による木の巡回
# LEFT=0
# RIGHT=1
# DATA=2

# node=[
#     [1,   2,   10],
#     [3,   4,   5,],
#     [5,  None, 12],
#     [None,None, 2],
#     [6,   7,    8],
#     [None,None,11],
#     [None,None, 6],
#     [None,None, 9]
# ]

# def traverse(p):
#     if p!=None:
#         traverse(node[p][LEFT])
#         print(node[p][DATA])
#         traverse(node[p][RIGHT])

# print("二分探索木を通り掛け順に巡回")
# traverse(0)

#=====数当てゲーム=====

import random

n=0
r=random.randint(1,100) #変数rに1~100の乱数を代入
print("1~100の数を当てるゲームです")

while True:
    n+=1
    a=int(input("数を入力してください"))
    if r==a:
        print(str(n)+"回で正解です")
        break
    if r>a:
        print("それより大きい数です")
    else:
        print("それより小さい数です")
