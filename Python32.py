#  write a program using function to find gratest of three number
def funct01(a,b,c):
    if a>b:
        f1=a
    elif b>a:
        f1=b
    if f1>c:
        f2=f1
    elif c>f1:
        f2=c
    print("The greatest number of these three is :",+f2)    
    
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
funct01(a,b,c)    