from os import write


def game():
    return 3999
score=game
with open('highscrore.txt') as f:
    highscorestr=f.read()
if highscorestr=='': 
    with open('highscrore.txt','w') as f:
        f.write(str(score))


