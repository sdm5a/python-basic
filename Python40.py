# to change the hiscore in a txt file by python
def game():
    return 25368935983356
score=game()
with open('heighscore.txt') as f:
    hiscore=(f.read())
if hiscore=="":
    with open('heighscore.txt','w') as f:
        f.write(str(score))    
        
elif int(hiscore)<score:
    with open('heighscore.txt','w') as f:
        f.write(str(score))    
