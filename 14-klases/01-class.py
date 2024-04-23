class Robotai: #be konstruktoriaus
    name = None
    age = None
    enable = None

dulkiuSiurblys = Robotai()
dulkiuSiurblys.name = 'Xiomi'
dulkiuSiurblys.age = 2
dulkiuSiurblys.enable = True

#nauja savybe ir verte
dulkiuSiurblys.color = 'Black'
print(dulkiuSiurblys)
print(dulkiuSiurblys.__dict__)

class Robotai2:
    def __init__(self, name, age, enable): #su konstruktorium
        self.name = name
        self.age = age
        self.enable = enable

    def startRobot(self, val, min):
        self.min = min
        self.val = val

    def getStartRobot(self):
        print(f'Sio roboto vardas {self.name}')
        return f'{self.val}:{self.min}'
    
dulkiuSiurblys = Robotai2('Xiaomi', 2, True)