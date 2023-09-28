import tkinter as tk
from random import randrange

wid = 780
hei = 500
velkost_gulicky=50
casovac=50
finalX= wid-velkost_gulicky
finalY= hei-2*velkost_gulicky
finalX2= 40
gulicky= []


root=tk.Tk()
root.title('goralky')
canvas = tk.Canvas(width = wid, height = hei)
canvas.pack()

img = tk.PhotoImage(file="koralik_nit.png")
canvas.create_image(0,hei-(1.75*velkost_gulicky), anchor='nw', image=img)

farby = ['red','blue','magenta','orange']

def goraliky():
    global gulicky
    for i in range(0,10):
        for i in farby:
            x = randrange(0,wid-velkost_gulicky)
            y = randrange(0,hei-3*velkost_gulicky)
            temp = canvas.create_oval(x,y, x+velkost_gulicky, y+velkost_gulicky, fill=i)
            gulicky.append(temp)
def kliknutie(e):
    pg=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if (len(pg))>0:
        #if pg[0] in gulicky
        moveit(pg[0])
def moveit(gulicky):
    global finalX2
    sur_gul = canvas.coords(gulicky)
    print(sur_gul)
    dx= abs(finalX-sur_gul[0])
    dy= abs(finalY-sur_gul[1])
    bx= 0
    if finalY== sur_gul[1]:
        if sur_gul[0] != finalX2:
            canvas.move(gulicky,-10,0)
            canvas.after(casovac, moveit, gulicky)
        else:
            finalX2 += 50
    elif dx > dy and (dx != 0 or dy != 0):
        posun= dx/dy
        canvas.move(gulicky,posun,1)
        canvas.after(casovac, moveit, gulicky)
    elif dx < dy and (dx != 0 or dy != 0):
        posun= dy/dx
        canvas.move(gulicky,1,posun)
        canvas.after(casovac, moveit, gulicky)


canvas.bind('<Button-1>',kliknutie)

goraliky()
root.mainloop()
