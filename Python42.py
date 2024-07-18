#  write a program to sensor a word dunkey written multiple times
with open('Sensor.txt','r') as f:
    content=f.read()
list=["suwar","kukur","pilla","hramkhor"]    
for words in list:
    content=content.replace(words,"@#$%^&*")
        
with open("Sensor.txt","w") as f:
    f.write(content)        
            