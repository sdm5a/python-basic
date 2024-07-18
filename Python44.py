# write a program using class and obj to fine sq. , cube , and sq.root of a number

class claculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"The square of {self.num} is {self.num**2}")
    def sq_root(self):
        print(f"The square root of {self.num} is {self.num**0.5}")
    def cube(self):
        print(f"The cube of {self.num} is {self.num**3}")
n=int(input("Enter any number: "))
a=claculator(n)
a.cube()    
a.sq_root()
a.square()                