# write a fuction to remove and strip a word from a list 
list=["Saddam","Awantika","Ritesh","Shashi","Rahul"]
def remove(w):
    list.remove(w)
print(list)    
w=input("Enter any word from these words:")    
w.strip()
remove(w)    
print(list)