# write a python function to print n lines of this pattern
'''
* * * * * 
* * * * 
* * * 
* * 
*  '''
n=int(input("Enter any number: "))
def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print("* ", end="")
        print()
            
pattern(n)            