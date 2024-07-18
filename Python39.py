f=open('poem.txt','r')
R=f.read()
if 'Twinkle' in R:
    print("Yes, Tweinkle is present.")
else:
    print("No, Twinkle is not present.") 
f.close()       