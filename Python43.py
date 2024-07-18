# creat a class of programer to store info of some programer working in microsoft
class programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def info(self):
        print(f"The name of the {self.company} programmer is {self.name} , and the product is {self.product}")    
        
saddam=programmer("Saddam","Skype")        
abc=programmer("Abc","Github")
saddam.info()
abc.info()