#3-1
#スタック

MAX=5
stack=[0]*MAX
sp=0 #データ出し入れ位置管理

def push(d):
    global sp
    if sp<MAX:
        stack[sp]=d
        sp=sp+1
        print("sp:",sp)
        print("データ",d,"を追加しました")
    else:
        print("これ以上は無理")

def pop():
    global sp
    if sp>0:
        print("sp:",sp)
        sp=sp-1
        
        return stack[sp]
    else:
        print("取り出すデータがない")
        return None
    
for i in range(6):
    push(i)
    
for j in range(6):
    d=pop()
    print("取り出したデータ:",d)
    
