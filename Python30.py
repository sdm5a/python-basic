# to find factorial of a given number
n=int(input("Enter any number: "))
fact=1
if n<0:
    print("Sorry factorial does not exist for this number.")
elif n==1 and n==0:
    print(f"Factorial is {fact}")    
else:
    for i in range(1,n+1):
        fact=fact*i
    print(f"Factorial of {n} is {fact}")            
