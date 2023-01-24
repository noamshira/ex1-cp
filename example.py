import sys
ls=['!', '@', '#' , '$', '%', '^', '&','*', '(',')','_']
print(ls)
print("enter a  passwpord")
ps=input()
length=len(ps)
if length<6:
    sys.exit("password not long enough")
f1=False
f2=False
f3=f2=False
for char in ps:
    if char.islower():
        f1=True
    elif char.isupper():
        f2=True
    elif char in ls:
        f3=True
    if char.isspace():
        sys.exit("password not illigal")
if f1 and f2 and f3:
    print("True")
else:print("False")









