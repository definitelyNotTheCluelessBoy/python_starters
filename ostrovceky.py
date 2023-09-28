import tkinter as tk
from random import randrange

M = randrange(4,7)
N = randrange(3,10)
sirka_platna= 1000
vyska_platna=500
status=0
spendings = 0

root=tk.Tk()
canvas= tk.Canvas(root,width=sirka_platna,height=vyska_platna)
canvas.pack()

def createland():
    global ostrovy, nic, prepinac, text
    for i in range(0,N):
        for j in range(0,M):
            temp= randrange(10,101)
            if temp<=20:
                ostrovy.append(canvas.create_image(j*50,i*50,image=ostrovy_zdroj[0],anchor='nw'))
            else:
                nic.append(canvas.create_image(j*50,i*50,image=ostrovy_zdroj[3],anchor='nw'))
    prepinac= canvas.create_image(sirka_platna-100,50,image=prepinac_zdroj[0],anchor='nw')
    text = canvas.create_text(sirka_platna-200,75,text = str(spendings),font=("Purisa", 60))

def zmenstatus():
    global status
    status= 1-status

def zmenobrazok(e):
    if(canvas.itemcget(prepinac,'image')=='pyimage5'):
        canvas.itemconfig(prepinac, image=prepinac_zdroj[1])
        zmenstatus()
    else:
        canvas.itemconfig(prepinac, image=prepinac_zdroj[0])
        zmenstatus()

def zmenmost(e):
    global nic, mosty, ostrovy
    pg = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)
    if len(pg) > 0:
        tag = (pg[0])
        if (canvas.itemcget(tag, 'image') == 'pyimage2') and status ==0:
            canvas.itemconfig(tag, image=ostrovy_zdroj[2])
        else:
            canvas.itemconfig(tag, image=ostrovy_zdroj[1])

def zmenostrov(e):
    global nic, mosty, ostrovy, spendings, text
    pg=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(pg)>0:
        tag=(pg[0])
        if status==1:
            nic.remove(tag)
            ostrovy.append(tag)
            canvas.itemconfig(tag, image= ostrovy_zdroj[0])
            canvas.tag_unbind(tag,'<Button-1>')
            spendings +=50
            canvas.itemconfig(text, text=str(spendings))
        elif status==0:
            nic.remove(tag)
            mosty.append(tag)
            canvas.itemconfig(tag, image=ostrovy_zdroj[1])
            canvas.tag_unbind(tag, '<Button-1>')
            spendings += 10
            canvas.itemconfig(text, text=str(spendings))
            for i in mosty:
                canvas.tag_bind(i, '<Button-1>', zmenmost)

ostrovy_zdroj= [tk.PhotoImage(file='ostrov0.png'),tk.PhotoImage(file='ostrov1.png'),tk.PhotoImage(file='ostrov2.png'), tk.PhotoImage(file='ostrov3.png')]
prepinac_zdroj= [tk.PhotoImage(file='ostrov_kruh0.png'), tk.PhotoImage(file='ostrov_kruh1.png')]

ostrovy = []
nic= []
mosty= []

createland()

canvas.tag_bind(prepinac,'<Button-1>',zmenobrazok)
for i in nic:
    canvas.tag_bind(i,'<Button-1>',zmenostrov)

root.mainloop()
