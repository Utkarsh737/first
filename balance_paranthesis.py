a=list(input("enter the string"))
flag=0
stack=[]
for i in a:
    if i == '('or i=='{'or i=='[':
        stack.append(i)
    else:
        if len(stack)==0:
            print(stack,i)
            print("unbalanced")
            flag=1
            break
        else:
            q=stack.pop()
            if( q=='(' and i!=')') or(q=='{' and i!='}') or(q=='[' and i!=']'):
                print(q)
                print("unbalanced")
                flag=1
                break
if len(stack)==0 and flag==0:
    print("Balanced")

    
