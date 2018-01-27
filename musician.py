class musician(object):
    
    def __init__(self, sounds):
        self.sounds = sounds
    
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i])
            
class Basinist(musician):
    
    def __init__(self):
        super().__init__(['twang','thrumb','bling'])
        
class Guitarist(musician):
    
    def __init__(self):
        super().__init__(['Boink', 'Bow','Boom'])
   
    def tune(self):
        print('Be with you in a momemt')
        print('Twoning, Sproing, Splang')
        
class Drummer(musician):
    
    def __init__(self):
        super().__init__(['Bop','Bump','Pow')]
    
    def solo(self):
        super().solo(3)
        
    def count():
        print("here we go boys")
        for num in range(1,4)
        print(num)
    
    def Combust():
        print('FIRE!!!!')
        
class Band(object):
    def __init__(self, musicians = []):
        self.musicians = musicians
        
    def hire(musician):
        self.musicians.append(musician)
    
    def fire(musician):
        self.musicians.remove(musician)
    
    def play(self)
        self.musicians = players
        for member in players:
            if players[member] = 'Drummer':
                players[member].count()
            players[member].solo()

john = Guitarist()
jerry = Basinist()
jones = Drummer()
rolling stones = Band(john,jerry,jones)
