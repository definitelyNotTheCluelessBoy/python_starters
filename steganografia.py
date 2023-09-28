#steganografia, skryvanie samotnej spravy
#kodovanie proces prevadzania nejakej spravy do inej abecedy, je prilozeny verejny kluc
#sifrovanie proces prevadzania nejakej spravy do inej abecedy, je prilozeny neverejny kluc, skryvanie obsahu spravy
# dva tipy syfrovania: symetricke (jeden kluc) a asymetricke (dva kluce, 1 verejny a 1 neverejny)

from PIL import Image

sprava = 'ahoj ako sa mas /*:iagjh;dkljga;dlgja;lgjuda;goldjga;lgjd;aljdglajgaljg;aj;jldgjahjkdghajhdgakjagdad 43a541 fsfa pa;dkhojlgdgljadg;ladgjadl;gadklkjgkadhfp;ojuajffffffffffffffffffffffasffssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss$'
obrazok= 'C:\\Users\\PC-Matúš\\PycharmProjects\\srandypandy\\textove\\master-oogway-quotes.png'

def zmen(sprava):
    temp = []
    for i in sprava:
        bn = bin(ord(i))[2::]
        if len(bn) == 6:
            temp.append(int(0))
            temp.append(int(0))
        else:
            temp.append(int(0))
        for j in bn:
            temp.append(int(j))
    return temp

def rozloz_dlzku(width,lenght):
    zoznam = []
    while lenght > width:
        zoznam.append(width)
        lenght-=width
    zoznam.append(lenght)
    return zoznam

def spracuj(sprava,obrazok):
    spracovanasprava= zmen(sprava)
    temp = Image.open(obrazok)
    polepixelov = temp.load()
    width = temp.size[0]
    rozlozenie = rozloz_dlzku(width,len(spracovanasprava))
    for i in range(0,len(rozlozenie)):
        for j in range(0,rozlozenie[i]):
            px = j
            py = i
            blue= polepixelov[px,py][2]
            if blue % 2 != spracovanasprava[j+(width*i)]:
                blue = blue // 2*2 + spracovanasprava[j+(width*i)]
            polepixelov[px, py]=(polepixelov[px,py][0],polepixelov[px,py][1],blue)
    temp.save('C:\\Users\\PC-Matúš\\PycharmProjects\\srandypandy\\textove\\hello.png','PNG')

spracovany_obrazok= 'C:\\Users\\PC-Matúš\\PycharmProjects\\srandypandy\\textove\\hello.png'

def znak(cislo):
    if cislo[0:2]=='00':
        a= int(cislo[2:8],2)
        return chr(a)
    else:
        a= int(cislo[1:8],2)
        return chr(a)

def desifruj(obrazok):
    sprava=''
    znakbin = ''
    pocitadlo = 0
    temp = Image.open(obrazok)
    polepixelov = temp.load()
    width = temp.size[0]
    height = temp.size[1]
    for i in range(0,height):
        for j in range(0,width):
            px = j
            py = i
            blue= polepixelov[px,py][2]
            if blue %2 ==0:
                znakbin+='0'
                pocitadlo+=1
            else:
                znakbin+='1'
                pocitadlo += 1
            if pocitadlo == 8:
                a= znak(znakbin)
                if a == '$':
                    break
                else:
                    sprava+= a
                    znakbin=''
                    pocitadlo=0
    print(sprava)
spracuj(sprava,obrazok)
desifruj(spracovany_obrazok)

