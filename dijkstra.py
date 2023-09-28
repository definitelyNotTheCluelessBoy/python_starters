subor = open('C:\\Users\\PC-Matúš\\PycharmProjects\\srandypandy\\textove\\ziaci.txt','r')

slovnik_hodnot={'Bratislava': {'Dunajská Streda': 104.69, 'Senec': 57.57, 'Malacky': 79.91}, 'Dunajská Streda': {'Bratislava': 104.69, 'Komárno': 117.35}, 'Komárno': {'Dunajská Streda': 117.35, 'Nové Zámky': 61.01, 'Štúrovo': 102.49}, 'Nové Zámky': {'Komárno': 61.01, 'Nitra': 90.26, 'Galanta': 97.35, 'Štúrovo': 113.15, 'Levice': 99.64}, 'Nitra': {'Nové Zámky': 90.26, 'Trnava': 93.56, 'Levice': 96.84, 'Topolčany': 69.43, 'Žiar nad Hronom': 157.0}, 'Trnava': {'Nitra': 93.56, 'Piešťany': 76.61, 'Senec': 54.2, 'Senica': 99.81}, 'Dudince': {'Levice': 54.34, 'Zvolen': 117.18, 'Lučenec': 152.11}, 'Levice': {'Dudince': 54.34, 'Nitra': 96.84, 'Štúrovo': 115.32, 'Nové Zámky': 99.64, 'Žiar nad Hronom': 110.07}, 'Topolčany': {'Nitra': 69.43, 'Prievidza': 100.69}, 'Prievidza': {'Topolčany': 100.69, 'Trenčin': 108.81, 'Žiar nad Hronom': 66.84, 'Žilina': 126.12}, 'Trenčin': {'Prievidza': 108.81, 'Piešťany': 87.66, 'Považská Bystrica': 95.67}, 'Piešťany': {'Trenčin': 87.66, 'Trnava': 76.61}, 'Senec': {'Trnava': 54.2, 'Bratislava': 57.57, 'Galanta': 59.68}, 'Malacky': {'Bratislava': 79.91, 'Kúty': 65.12}, 'Kúty': {'Malacky': 65.12, 'Skalica': 61.55}, 'Skalica': {'Kúty': 61.55, 'Senica': 43.42}, 'Senica': {'Skalica': 43.42, 'Trnava': 99.81}, 'Považská Bystrica': {'Trenčin': 95.67, 'Žilina': 62.18}, 'Žilina': {'Považská Bystrica': 62.18, 'Čadca': 61.52, 'Martin': 51.22, 'Prievidza': 126.12}, 'Čadca': {'Žilina': 61.52}, 'Martin': {'Žilina': 51.22, 'Ružomberok': 70.06, 'Turčianske Teplice': 63.06}, 'Ružomberok': {'Martin': 70.06, 'Dolný Kubín': 38.05, 'Liptovský Mikuláš': 55.04, 'Banská Bystrica': 100.28}, 'Dolný Kubín': {'Ružomberok': 38.05, 'Námestovo': 54.71}, 'Námestovo': {'Dolný Kubín': 54.71}, 'Liptovský Mikuláš': {'Ružomberok': 55.04, 'Poprad': 122.1, 'Brezno': 76.06}, 'Poprad': {'Liptovský Mikuláš': 122.1, 'Stará Ľubovňa': 96.94, 'Prešov': 171.35, 'Tisovec': 122.45, 'Rožňava': 120.7}, 'Stará Ľubovňa': {'Poprad': 96.94, 'Plaveč': 36.69}, 'Bardejov': {'Svidník': 54.33, 'Plaveč': 70.71}, 'Svidník': {'Bardejov': 54.33, 'Stropkov': 36.24}, 'Stropkov': {'Svidník': 36.24, 'Prešov': 89.81}, 'Prešov': {'Stropkov': 89.81, 'Poprad': 171.35, 'Košice': 77.32, 'Humenné': 118.83, 'Plaveč': 99.7}, 'Košice': {'Prešov': 77.32, 'Michalovce': 116.97, 'Rožňava': 135.15}, 'Michalovce': {'Košice': 116.97, 'Humenné': 48.26}, 'Humenné': {'Michalovce': 48.26, 'Prešov': 118.83, 'Snina': 54.08}, 'Rožňava': {'Košice': 135.15, 'Rimavská Sobota': 118.7, 'Poprad': 120.7}, 'Rimavská Sobota': {'Rožňava': 118.7, 'Lučenec': 63.15, 'Tisovec': 83.55}, 'Lučenec': {'Rimavská Sobota': 63.15, 'Dudince': 152.11, 'Detva': 75.01}, 'Zvolen': {'Banská Bystrica': 46.17, 'Žiar nad Hronom': 50.09, 'Dudince': 117.18, 'Detva': 50.25}, 'Banská Bystrica': {'Zvolen': 46.17, 'Brezno': 89.74, 'Ružomberok': 100.28, 'Turčianske Teplice': 65.37}, 'Brezno': {'Banská Bystrica': 89.74, 'Tisovec': 65.51, 'Liptovský Mikuláš': 76.06}, 'Žiar nad Hronom': {'Zvolen': 50.09, 'Prievidza': 66.84, 'Nitra': 157.0, 'Turčianske Teplice': 75.06, 'Levice': 110.07}, 'Štúrovo': {'Komárno': 102.49, 'Levice': 115.32, 'Nové Zámky': 113.15}, 'Detva': {'Zvolen': 50.25, 'Lučenec': 75.01}, 'Tisovec': {'Rimavská Sobota': 83.55, 'Brezno': 65.51, 'Poprad': 122.45}, 'Galanta': {'Nové Zámky': 97.35, 'Senec': 59.68}, 'Plaveč': {'Stará Ľubovňa': 36.69, 'Bardejov': 70.71, 'Prešov': 99.7}, 'Snina': {'Humenné': 54.08}, 'Turčianske Teplice': {'Banská Bystrica': 65.37, 'Martin': 63.06, 'Žiar nad Hronom': 75.06}}

# for i in subor:
#     riadok= i.rstrip().split(';')
#     if riadok[0] not in slovnik_hodnot:
#         slovnik_hodnot[riadok[0]]={riadok[1]:int(riadok[2])}
#     if riadok[1] not in slovnik_hodnot:
#         slovnik_hodnot[riadok[1]]={riadok[0]:int(riadok[2])}
#     if riadok[0] in slovnik_hodnot:
#         slovnik_hodnot[riadok[0]] = {**slovnik_hodnot[riadok[0]],**{riadok[1]: int(riadok[2])}}
#     if riadok[1] in slovnik_hodnot:
#         slovnik_hodnot[riadok[1]] = {**slovnik_hodnot[riadok[1]],**{riadok[0]: int(riadok[2])}}

map= {}
for i in slovnik_hodnot:
    map[i]={'predosly':None,'vzdialenost':None}
mapa=map

start='Bratislava'
koniec='Košice'
navstivene=[]
na_prehladanie=[]

mapa[start]['vzdialenost']=0
for i in slovnik_hodnot[start]:
    mapa[i]['vzdialenost']= mapa[start]['vzdialenost']+int(slovnik_hodnot[start][i])
    mapa[i]['predosly'] = start
    na_prehladanie.append(i)
navstivene.append(start)

while len(na_prehladanie) != 0:
    for j in na_prehladanie:
        zoznam = []
        for i in na_prehladanie:
            zoznam.append(mapa[i]['vzdialenost'])
        if mapa[j]['vzdialenost'] == min(zoznam):
            for i in slovnik_hodnot[j]:
                if mapa[i]['vzdialenost']==None:
                    mapa[i]['vzdialenost'] = mapa[j]['vzdialenost'] + int(slovnik_hodnot[j][i])
                    mapa[i]['predosly'] = j
                elif mapa[i]['vzdialenost']> (mapa[j]['vzdialenost'] + int(slovnik_hodnot[j][i])):
                    mapa[i]['vzdialenost'] = mapa[j]['vzdialenost'] + int(slovnik_hodnot[j][i])
                    mapa[i]['predosly'] = j
                if i not in navstivene:
                    if i not in na_prehladanie:
                        na_prehladanie.append(i)
            navstivene.append(j)
            na_prehladanie.remove(j)

predosli= koniec
cesta=[]
while predosli!=None:
    cesta.append(predosli)
    predosli=mapa[predosli]['predosly']
print(cesta[::-1],mapa[koniec]['vzdialenost'])