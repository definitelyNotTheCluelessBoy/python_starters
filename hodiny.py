import tkinter as tki
import datetime
root = tki.Tk()
canvas = tki.Canvas(width = 500, height = 500)
canvas.pack()

class Ciara:

    def __init__(self,x,y,dx,dy,farba):
        self.id = canvas.create_rectangle(x,y,x+dx,y+dy,fill = farba, outline = farba)

    def turnOff(self):
        canvas.itemconfigure(self.id, state = "hidden")

    def turnOn(self):
        canvas.itemconfigure(self.id, state = "normal")

class Segment:
    # sirka a dlzka tej ciary
    def __init__(self,x,y,sirka,dlzka,farba):
        self.ciary = []
        self.ciary.append(Ciara(x+sirka, y, dlzka, sirka,farba))
        self.ciary.append(Ciara(x+sirka+dlzka,y+sirka,sirka,dlzka,farba))
        self.ciary.append(Ciara(x+sirka, y+dlzka+sirka, dlzka, sirka, farba ))
        self.ciary.append(Ciara(x,y+sirka,sirka,dlzka,farba))
        self.ciary.append(Ciara(x + sirka + dlzka, y + 2 * sirka + dlzka, sirka, dlzka, farba))
        self.ciary.append(Ciara(x + sirka, y + 2 * sirka + 2 * dlzka, dlzka, sirka, farba))
        self.ciary.append(Ciara(x, y + 2 * sirka + dlzka, sirka, dlzka, farba))

    def reset(self):
        for i in self.ciary:
            i.turnOff()

    def turnOn(self):
        for i in self.ciary:
            i.turnOn()

    def zobraz(self,cislo):
        if cislo == 0:
            self.turnOn()
            self.ciary[2].turnOff()
        if cislo == 1:
            self.reset()
            self.ciary[1].turnOn()
            self.ciary[4].turnOn()
        if cislo == 2:
            self.turnOn()
            self.ciary[3].turnOff()
            self.ciary[4].turnOff()
        if cislo == 3:
            self.turnOn()
            self.ciary[3].turnOff()
            self.ciary[6].turnOff()
        if cislo == 4:
            self.turnOn()
            self.ciary[0].turnOff()
            self.ciary[6].turnOff()
            self.ciary[5].turnOff()
        if cislo == 5:
            self.turnOn()
            self.ciary[1].turnOff()
            self.ciary[6].turnOff()
        if cislo == 6:
            self.turnOn()
            self.ciary[1].turnOff()
        if cislo == 7:
            self.reset()
            self.ciary[0].turnOn()
            self.ciary[1].turnOn()
            self.ciary[4].turnOn()
        if cislo == 8:
            self.turnOn()
        if cislo == 9:
            self.turnOn()
            self.ciary[6].turnOff()

class Display:
    def __init__(self,x,y,sirka,dlzka,farba):
        offset= dlzka*(2/5)
        self.segmenty = []
        self.segmenty.append(Segment(x,y,sirka,dlzka,farba))
        self.segmenty.append(Segment(x+dlzka+offset, y, sirka, dlzka, farba))
        self.segmenty.append(Segment(x + 2*dlzka + 3*offset, y, sirka, dlzka, farba))
        self.segmenty.append(Segment(x + 3 * dlzka + 4*offset, y, sirka, dlzka, farba))
        self.segmenty.append(Segment(x + 4 * dlzka + 6* offset, y+dlzka, sirka, dlzka/2, farba))
        self.segmenty.append(Segment(x + 4.5 * dlzka + 7*offset, y+dlzka, sirka, dlzka / 2, farba))
        self.bodky()

    def bodky(self):
        canvas.create_rectangle(190, 140, 200, 150, fill='green', outline='green')
        canvas.create_rectangle(190, 170, 200, 180, fill='green', outline='green')

    def zobraz(self):
        #self.bodky()
        now = datetime.datetime.now()
        cas = now.hour*10000+ now.minute*100+ now.second
        for i in range(len(self.segmenty)):
            self.segmenty[i].zobraz(int(str(cas)[i]))

    def tiktik(self):
        self.zobraz()
        canvas.update()
        canvas.after(100,self.tiktik)


#ciara1 = Ciara(0,0,5,50,"red")
#ciara1.turnOff()
#ciara2 = Ciara(100,100,50,5,"blue")

#segment1 = Segment(1,1,5,50,"green")
#segment1.zobraz(0)

#canvas.create_rectangle(190, 140, 200, 150, fill='green', outline='green')
#canvas.create_rectangle(190, 170, 200, 180, fill='green', outline='green')

display1=Display(50,100,5,50,'green')
display1.tiktik()

root.mainloop()