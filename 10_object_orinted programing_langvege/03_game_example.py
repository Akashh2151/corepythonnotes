class remote():
    pass
class player:
    def moveright(self):
        pass
    
    def moveleft(self):
        pass
    
    def movetop(self):
        pass

remote1=remote()   # covert into object
player1=player()   # convert into object
if(remote1.isleftpressed()):
    player1.moveleft()