# write a python function to print table of given number
def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
n=int(input("Enter any number :"))        
table(n)