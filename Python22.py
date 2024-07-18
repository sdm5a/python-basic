# write a program to find greatest out of four number
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
d=int(input("Enter fourth number: "))
if a>b:
    f1=a
else:
    f1=b
if c>d:
    f2=c
else:
    f2=d
if f1>f2:
    print(f"Greatest number is ",f1)
else:
    print(f"Greatest number is ",f2)                    
