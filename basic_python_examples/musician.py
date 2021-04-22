class Musician(object):
    
    def __init__(self, sounds):
        self.sounds = sounds
    
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i])
            
class Basinist(Musician):
    
    def __init__(self):
        super().__init__(['twang','thrumb','bling'])
        
class Guitarist(Musician):
    
    def __init__(self):
        super().__init__(['Boink', 'Bow','Boom'])
   
    def tune(self):
        print('Be with you in a momemt')
        print('Twoning, Sproing, Splang')
        
class Drummer(Musician):
    
    def __init__(self):
        super().__init__(['Bop','Bump','Pow'])

    def solo(self, count):
        super().solo(3)
        
    def count():
        print("here we go boys")
        for num in range(1,4):
            print(num)
    
    def Combust():
        print('FIRE!!!!')
        
class Band(object):
    def __init__(self):
        self.the_drummer = None
        self.musicians = []
        
        
    def hire(self, musician):
        if isinstance(musician, list) == False:
            musician = [musician]
            
        for new_member in musician:
            if isinstance(musician, Drummer):
                self.the_drummer = musician
            self.musicians.append(new_member)
            
    def fire(musician):
        self.musicians.remove(musician)
    
    def play(self):
        if self.the_drummer != None:
            self.the_drummer.count()
        
        for member in self.musicians:
            member.solo(1)

john = Guitarist()
jerry = Basinist()
jones = Drummer()
rolling_stones = Band()
rolling_stones.hire([john, jerry, jones])
rolling_stones.play()
