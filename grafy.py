import tkinter as tk    # gui (cez command je to CLI
root = tk.Tk()
sirka = 1100
vyska = 600
velkost = 10
can = tk.Canvas(width = sirka, height = vyska)
can.pack()

def nacitaj(subor):
    data = open(subor, "r",encoding = "utf-8")
    slovnik = {}
    for i in data:
        mesto = i.split(";")[0]
        suradnice = (int(i.split(";")[1]),int(i.split(";")[2]))
        slovnik[mesto] = suradnice

    return slovnik

def boduj(slovnik):
    zoz = []
    for sur in slovnik:
        x = int(slovnik[sur][0])
        y = int(slovnik[sur][1])
        zoz.append([can.create_oval(x-(velkost//2),y-(velkost//2),x+(velkost//2),y+(velkost//2),fill = "blue"),sur])
        can.create_text(x,y+velkost,text = sur)

    return slovnik, zoz

mapa = nacitaj("C:\\Users\\Matúš\\Desktop\\Škola\\Informatika\\Python projekty\\textove")
slovnik = boduj(mapa)
print(boduj(mapa))

def zarad_do_grafu(odkial,kam,graf):
    if odkial not in graf:
        graf[odkial] = [kam]
    else:
        if kam not in graf[odkial]:
            graf[odkial].append(kam)

def hrany(slovnik,hrany):
    file = open(hrany,"r",encoding = "utf-8")
    lajny = []
    graf = {}
    for i in file:
        mesto_A = i.split(";")[0].strip()
        mesto_B = i.split(";")[1].strip()
        zarad_do_grafu(mesto_A,mesto_B,graf)
        zarad_do_grafu(mesto_B, mesto_A,graf)
        for mesto in slovnik:
            if mesto == mesto_A:
                prve = slovnik[mesto]
            if mesto == mesto_B:
                druhe = slovnik[mesto]
        lajny.append( can.create_line(prve[0],prve[1],druhe[0],druhe[1]) )
    return graf

graf = hrany(slovnik[1], "C:\\Users\\Matúš\\Desktop\\Škola\\Informatika\\Python projekty\\textove")

# def trojuholnik(graf):
#     for i in graf:
#         for j in graf[i]:
#             for k in graf[j]:
#                 if i in graf[k]:
#                     print(i,j,k)
# trojuholnik(graf)

# def do_hlbky(mesto,navstivene):
#     navstivene.append(mesto)
#     for i in graf[mesto]:
#         if i not in navstivene:
#             print(i)
#             do_hlbky(i,navstivene)
# do_hlbky('Bratislava',[])


# def prekresli(mesto):
#     for i in zoz:
#         if mesto in i:
#             can.itemconfig

def prehladavanieDoSirky(mesto):
    temp = []; temp.append(mesto)
    visited = []; visited.append(mesto)
    while temp != []:
        print(temp[0])
        for i in graf[temp[0]]:
            if i not in visited:
                temp.append(i)
                visited.append(i)
        temp.pop(0)
prehladavanieDoSirky("Bratislava")
root.mainloop()
