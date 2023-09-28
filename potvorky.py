import random

class Potvorka:
    def __init__(self,code=None):
        self.id = code
        if not code:
            self.id=[]
            for i in range(5):
                self.id.append(random.randint(1,10))

    def krasa(self):
        #return self.id.count(10)
        k=0
        etalonKrasy=[10,10,10,10,10]
        for i in zip(etalonKrasy,self.id):
            if i[0]==i[1]:
                k+=1
        return k

    def mnozenie(self,p2):
        potvorka = []
        for i in range(5):
            fs = random.randint(1,2)
            mutagen=random.randint(1,25)
            if mutagen == 1:
                potvorka.append(random.randint(0,10))
            elif fs == 1:
                potvorka.append(self.id[i])
            else:
                potvorka.append(p2.id[i])
        return Potvorka(potvorka)

class CernobylSvorka:
    def __init__(self):
        self.kosiar=[]
        for i in range(10):
            self.kosiar.append(Potvorka())
    def vypisPotvorky(self):
        for i in self.kosiar:
            print(i.id)
    def selekcia(self):
        self.kosiar.sort(key= lambda x: x.krasa(),reverse=True)
        for i in range(5):
            self.kosiar.pop()
    def spajanie(self):
        for i in range(5):
            p1 = random.choice(self.kosiar)
            p2 = random.choice(self.kosiar)
            potomok = p1.mnozenie(p2)
            self.kosiar.append(potomok)


p1=Potvorka()
p2=Potvorka()
svorka=CernobylSvorka()
# print(p1.id)
# print(p2.id)
# print(p1.mnozenie(p2))
# svorka.selekcia()
# svorka.vypisPotvorky()
iteracia=0
while(True):
    print(iteracia)
    iteracia+=1
    svorka.selekcia()
    svorka.spajanie()
    svorka.vypisPotvorky()
    print('-----------------------')
    input()