import tkinter as tk
root = tk.Tk()
sirka = 1100
vyska = 700
velkost=18
can = tk.Canvas(height= vyska, width= 600)
can.pack()
def nacitaj(subor):
    data=open(subor,'r')
    slovnik={}
    for i in data:
        mesto = i.split(';')[0]
        suradnice= int(i.split(';')[1]),int(i.split(';')[2])
        slovnik[mesto]=suradnice
    return slovnik

def kresli(slovnik):
    zoz=[]
    for sur in slovnik:
        x= int(slovnik[sur][0])
        y= int(slovnik[sur][1])
        zoz.append(can.create_oval(x-(velkost//2),y-(velkost//2),x+(velkost//2),y+(velkost//2),fill='blue'))
        can.create_text(x,y+velkost,text=sur)

def hrany(slovnik):
    file = open('C:\\Users\\PC-Matúš\\PycharmProjects\\srandypandy\\textové\\hrany.txt', 'r')
    lajny = []
    graf={}
    for i in file:
        mesto_A = i.split(';')[0]
        mesto_B = i.split(';')[1]
        zarad_do_grafu(mesto_A,mesto_B,graf)
        zarad_do_grafu(mesto_B, mesto_A, graf)
        prve,druhe=(),()
        for mesto in slovnik:
            if mesto== mesto_A:
                prve=slovnik[mesto]
            if mesto == mesto_B:
                druhe = slovnik[mesto]
        lajny.append(can.create_line(prve[0],prve[1],druhe[0],druhe[1]))
    return graf


def zarad_do_grafu(mestoA,mestoB,graf):
    if mestoA not in graf:
        graf[mestoA]=[mestoB]
    else:
        if mestoB in graf[mestoA]:
            graf[mestoA].append(mestoB)
mapa=nacitaj('C:\\Users\\PC-Matúš\\PycharmProjects\\srandypandy\\textové\\vrcholy.txt')
kresli(mapa)
hrany(mapa)
graf=hrany(mapa)
print(graf)
root.mainloop()
