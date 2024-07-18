# write a recursive funtion to find sum of n number
def funct03(n):
    sum=0
    if n==0:
      return 0
    sum=n+funct03(n-1)
    return sum
n=int(input("Enter the value of n: "))
print(funct03(n)) 