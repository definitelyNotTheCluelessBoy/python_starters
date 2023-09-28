import tkinter as tk
root=tk.Tk()
wid = 330
hei = 330
canvas = tk.Canvas(root,width = wid, height = hei)
canvas.pack()

velkost_policka=40
switcher=0
pocitadlo=0
vstup = int(input('chcem pokus cislo: '))

def sachovnica1(rozmer):
    sachovnica=[]
    for i in range(rozmer):
        temp=[]
        for j in range(rozmer):
            temp.append(0)
        sachovnica.append(temp)
    return sachovnica
sachovnica=sachovnica1(8)

def pozadie(suradnice):
    switcher=0
    caunter0=5
    for i in suradnice:
        caunter1=5
        for j in i:
            if switcher == 1:
                canvas.create_rectangle(caunter1, caunter0,caunter1+velkost_policka,caunter0+velkost_policka,fill='black')
                caunter1+=velkost_policka
                switcher=1-switcher
            else:
                caunter1 += velkost_policka
                switcher=1-switcher
        caunter0+=velkost_policka
        switcher = 1 - switcher
pozadie(sachovnica)

def vytvor_damy(suradnice):
    switcher = 0
    caunter0=5
    for i in suradnice:
        caunter1=5
        for j in i:
            if j == 1:
                canvas.create_oval(caunter1, caunter0, caunter1 + velkost_policka, caunter0 + velkost_policka,fill='red')
                caunter1+=velkost_policka
                switcher = 1 - switcher
            else:
                caunter1 += velkost_policka
                switcher = 1 - switcher
        caunter0+=velkost_policka
        switcher = 1 - switcher

def checkIt(x,y):
    for i in range(len(sachovnica)):
        for j in range(len(sachovnica[i])):
            if x==j or y ==i or x-y==j-i or x+y==j+i:
                if sachovnica[i][j]==1:
                    return False
    return True

def pokladanie(cislo_dami):
    global pocitadlo
    if cislo_dami == 8:
        pocitadlo+=1
        print(sachovnica,pocitadlo)
        if vstup == pocitadlo:
            vytvor_damy(sachovnica)
    else:
        for i in range(0,8):
            if checkIt(i,cislo_dami):
                sachovnica[cislo_dami][i]=1
                pokladanie(cislo_dami+1)
                sachovnica[cislo_dami][i]=0
pokladanie(0)

root.mainloop()
