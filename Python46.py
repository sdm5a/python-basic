class train:
    def __init__(self,name,seats):
        self.name=name
        self.seats=seats
        
    def status(self):
        print(f"The train is {self.name} and the total seats is {self.seats}")
        
    def booking(self):
        if self.seats>0:
            print(f"Booking confirm and your seat number is {self.seats}")        
            self.seats=self.seats-1
        else:
            print("Seats not available")    
t1=train("Tapti Ganga express 19045",300)        
t1.status()
t1.booking()
t1.booking()