print("enter the numbers")
k=int(input())
print('enter your message')
message=input()
def cropping(message,k):
    l=len(message)
    if l==k:
        return (message)
    else:
        str=message[0:k]
    if message[k] or message[k+1]==' ':
        return str
    flag=False
    while flag == False:
        k=k-1
        if message[k]==' ':
            str=message[0:k]
            flag=True

    return str
str=cropping(message,k)
print(str)





