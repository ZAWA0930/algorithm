# import random 

# #Bogoソート
# #ボゴソートはシャッフルに並び替えた後にそのソートが正しく並び替えられているかを確認するソート手法

# def in_order(numbers):
#     for i in range(len(numbers)-1):
#         if numbers[i] > numbers[i+1]:
#             return False

# def bogo_sort(numbers):
#     random.shuffle(numbers)
#     return numbers

# if __name__=='__main__':
#     print(bogo_sort([1,5,3,2,6]))


# score = [70,98,92,88,64]
# total=0

# for i in range(5):
#     total=total+score[i]

# average=total/5

# print("合計点:" ,total)
# print("平均点:", average)


# a=0
# for i in range(1,11):
#     a=a+i
    
# print(a)

# def addup(n):
#     a=0
#     for i in range(1,n+1):
#         a=a+i
    
#     return a

# print(addup(10))

# def add_other(n):
#     a=(1+n)*(n/2)
#     return int(a)

# print(add_other(100))

# for i in range(1,10):
#     for j in range(1,10):
#         print(i,"x",j ,"=",i*j)

# for i in range(1,10):
#     k=""
#     for j in range(1,10):
#         k=k+"{}×{}={:2d} ".format(j,i,j*i)
#     print(k)

#素数
# for i in range(2,101):
#     h=i//2
#     f=True
#     for j in range(2,h+1):
#         if i%j==0:
#             f=False
#             break
#     if f==True:
#         print(i,end=" ")


#n!

# a=10
# for i in range(9,0,-1): #9から1まで1ずつ減る
#     a=a*i
# print("10!:",a)

# a=[10,-5,0,29,6,2,77,8]

# for i in a:
#     if i%2==0:
#         print(f"{i}は偶数です")
#     else:
#         print(f"{i}は奇数です")


#=====スタック=====
# MAX=5    #スタックデータ総数を定義
# stack=[0]*MAX #スタック用配列用意
# sp=0 #データの出し入れ位置管理変数

# def push(d):
#     global sp
#     if sp <MAX:
#         stack[sp]=d
#         sp=sp+1
#         print("データ", d,"追加しました")
#     else:
#         print("これ以上データを入れられません")

# def pop():
#     global sp
#     if sp>0:
#         sp=sp-1
#         return stack[sp]
#     else:
#         print("取り出すデータが存在しません:")
#         return None

# for i in range(6):
#     push(i)

# for i in range(6):
#     d=pop()
#     print("取り出したデータ",d)



#=====キュー=====
# MAX =6  #キューのでーたの総数+1を定義

# que=[0]*MAX
# head=0 #データを取り出す位置を管理する変数
# tail=0 #データを入れる位置を管理する変数

# def enqueue(d):
#     global tail
#     nt=(tail+1)%MAX
    
#     if nt==head:
#         print("これ以上はデータを入れられません")
#     else:
#         que[tail]=d
#         tail =nt
#         print("データ",d,"を追加しました")
        
# def dequeue():
#     global head
#     if head==tail:
#         print("取り出すデータが存在しません")
#         return None
#     else:
#         d=que[head]
#         head=(head+1)%MAX
#         return d

# for i in range(6):
#     enqueue(i)

# for i in range(6):
#     d=dequeue()
    
#     print("取り出したデータ",d)


# MAX=5
# data=[None]*MAX

# pointer=[None]*MAX
# head=0

# def add_list(d):
#     n=-1
#     for i in range(MAX):
#         if data[i]==None:
#             n=i
#             print(n)
#             break
    
#     if n==-1:
#         print("データに空きがありません")
#         return False
    
#     for i in range(MAX):
#         if data[i]!=None and pointer[i]==None:
#             pointer[i]=n
#             break
#     data[n]=d
#     pointer[n]=None
#     print("データ",d,"を追加しました")
#     print(data)
#     print(pointer)
#     return True

# def del_list(d):
#     global head
#     n=-1
#     for i in range(MAX):
#         if data[i]==d:
#             n=i
#             break
#     if n==-1:
#         print("そのデータは存在しません")
#         return False
#     if n!=head:
#         for i in range(MAX):
#             if pointer[i]==n:
#                 pointer[i]=pointer[n]
#     else:
#         head=pointer[n]
#         if head==None:
#             head=0
#     data[n]=None
#     pointer[n]=None
#     print("データ",d,"を削除しました")
#     return True

# def put_list():
#     p=head
#     while True:
#         print(data[p], end="→")
#         if pointer[p]==None:
#             print("EOF")
#             break
#         p=pointer[p]

# for i in range(10,70,10):
#     add_list(i)

# del_list(10)
# put_list()

# data=[
#     [0,1,1,0,0],
#     [0,0,1,1,0],
#     [0,0,0,0,0],
#     [0,0,0,0,1],
#     [0,0,1,1,0]
# ]

# node=["(0)","(1)","(2)","(3)","(4)"]
# arrow = ["","-->","<--","<->"]

# for y in range(5):
#     for x in range(y,5):
#         e1=data[y][x]
#         e2=data[x][y]
#         a=e1+e2*2
#         if a>0:
#             print(node[y]+arrow[a]+node[x])

#===素数===
#2~100までの素数を求める
for i in range(2,10):
    h=i//2
    f=True
    print("i:",i)
    print("h:",h)
    for j in range(2,h+1):
        if i%j==0:
            f=False
            break
    if f==True:
        #print(i,end=",")
        print(i)