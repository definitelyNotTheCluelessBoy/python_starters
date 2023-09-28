tabulka = {'Normal': {'Normal': 1.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Dragon': 1.0, 'Dark': 1.0, 'Fairy': 1.0, 'Rock': 0.5, 'Steel': 0.5, 'Ghost': 0.0}, 'Fire': {'Grass': 2.0, 'Ice': 2.0, 'Bug': 2.0, 'Steel': 2.0, 'Normal': 1.0, 'Electric': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Ghost': 1.0, 'Dark': 1.0, 'Fairy': 1.0, 'Fire': 0.5, 'Water': 0.5, 'Rock': 0.5, 'Dragon': 0.5}, 'Water': {'Fire': 2.0, 'Ground': 2.0, 'Rock': 2.0, 'Normal': 1.0, 'Electric': 1.0, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Ghost': 1.0, 'Dark': 1.0, 'Steel': 1.0, 'Fairy': 1.0, 'Water': 0.5, 'Grass': 0.5, 'Dragon': 0.5}, 'Electric': {'Water': 2.0, 'Flying': 2.0, 'Normal': 1.0, 'Fire': 1.0, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 1.0, 'Dark': 1.0, 'Steel': 1.0, 'Fairy': 1.0, 'Electric': 0.5, 'Grass': 0.5, 'Dragon': 0.5, 'Ground': 0.0}, 'Grass': {'Water': 2.0, 'Ground': 2.0, 'Rock': 2.0, 'Normal': 1.0, 'Electric': 1.0, 'Ice': 1.0, 'Fighting': 1.0, 'Psychic': 1.0, 'Ghost': 1.0, 'Dark': 1.0, 'Fairy': 1.0, 'Fire': 0.5, 'Grass': 0.5, 'Poison': 0.5, 'Flying': 0.5, 'Bug': 0.5, 'Dragon': 0.5, 'Steel': 0.5}, 'Ice': {'Grass': 2.0, 'Ground': 2.0, 'Flying': 2.0, 'Dragon': 2.0, 'Normal': 1.0, 'Electric': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 1.0, 'Dark': 1.0, 'Fairy': 1.0, 'Fire': 0.5, 'Water': 0.5, 'Ice': 0.5, 'Steel': 0.5}, 'Fighting': {'Normal': 2.0, 'Ice': 2.0, 'Rock': 2.0, 'Dark': 2.0, 'Steel': 2.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Fighting': 1.0, 'Ground': 1.0, 'Dragon': 1.0, 'Poison': 0.5, 'Flying': 0.5, 'Psychic': 0.5, 'Bug': 0.5, 'Fairy': 0.5, 'Ghost': 0.0}, 'Poison': {'Grass': 2.0, 'Fairy': 2.0, 'Normal': 1.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Ice': 1.0, 'Fighting': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Dragon': 1.0, 'Dark': 1.0, 'Poison': 0.5, 'Ground': 0.5, 'Rock': 0.5, 'Ghost': 0.5, 'Steel': 0.0}, 'Ground': {'Fire': 2.0, 'Electric': 2.0, 'Poison': 2.0, 'Rock': 2.0, 'Steel': 2.0, 'Normal': 1.0, 'Water': 1.0, 'Ice': 1.0, 'Fighting': 1.0, 'Ground': 1.0, 'Psychic': 1.0, 'Ghost': 1.0, 'Dragon': 1.0, 'Dark': 1.0, 'Fairy': 1.0, 'Grass': 0.5, 'Bug': 0.5, 'Flying': 0.0}, 'Flying': {'Grass': 2.0, 'Fighting': 2.0, 'Bug': 2.0, 'Normal': 1.0, 'Fire': 1.0, 'Water': 1.0, 'Ice': 1.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Ghost': 1.0, 'Dragon': 1.0, 'Dark': 1.0, 'Fairy': 1.0, 'Electric': 0.5, 'Rock': 0.5, 'Steel': 0.5}, 'Psychic': {'Fighting': 2.0, 'Poison': 2.0, 'Normal': 1.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 1.0, 'Dragon': 1.0, 'Fairy': 1.0, 'Psychic': 0.5, 'Steel': 0.5, 'Dark': 0.0}, 'Bug': {'Grass': 2.0, 'Psychic': 2.0, 'Dark': 2.0, 'Normal': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Ice': 1.0, 'Ground': 1.0, 'Bug': 1.0, 'Rock': 1.0, 'Dragon': 1.0, 'Fire': 0.5, 'Fighting': 0.5, 'Poison': 0.5, 'Flying': 0.5, 'Ghost': 0.5, 'Steel': 0.5, 'Fairy': 0.5}, 'Rock': {'Fire': 2.0, 'Ice': 2.0, 'Flying': 2.0, 'Bug': 2.0, 'Normal': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Poison': 1.0, 'Psychic': 1.0, 'Rock': 1.0, 'Ghost': 1.0, 'Dragon': 1.0, 'Dark': 1.0, 'Fairy': 1.0, 'Fighting': 0.5, 'Ground': 0.5, 'Steel': 0.5}, 'Ghost': {'Psychic': 2.0, 'Ghost': 2.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Bug': 1.0, 'Rock': 1.0, 'Dragon': 1.0, 'Steel': 1.0, 'Fairy': 1.0, 'Dark': 0.5, 'Normal': 0.0}, 'Dragon': {'Dragon': 2.0, 'Normal': 1.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 1.0, 'Dark': 1.0, 'Steel': 0.5, 'Fairy': 0.0}, 'Dark': {'Psychic': 2.0, 'Ghost': 2.0, 'Normal': 1.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 1.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Bug': 1.0, 'Rock': 1.0, 'Dragon': 1.0, 'Steel': 1.0, 'Fighting': 0.5, 'Dark': 0.5, 'Fairy': 0.5}, 'Steel': {'Ice': 2.0, 'Rock': 2.0, 'Fairy': 2.0, 'Normal': 1.0, 'Grass': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Ghost': 1.0, 'Dragon': 1.0, 'Dark': 1.0, 'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Steel': 0.5}, 'Fairy': {'Fighting': 2.0, 'Dragon': 2.0, 'Dark': 2.0, 'Normal': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 1.0, 'Fairy': 1.0, 'Fire': 0.5, 'Poison': 0.5, 'Steel': 0.5}}

vstup = open('C:\\Users\\PC-Matúš\\PycharmProjects\\srandypandy\\textove\\kekwmoni.txt','r')
subor = vstup.read().split('\n')
moji_pokemoni= subor[2:2+int(subor[0])]
moja_sila=0
nepriatelia = subor[2+int(subor[0]):]
nepritelska_sila=0

print(moji_pokemoni,nepriatelia)


for i in moji_pokemoni:
    for j in nepriatelia:
        if len(i.split())==2 and len(j.split())==2:
            moja_sila+= max(tabulka[i.split()[0]][j.split()[0]]*tabulka[i.split()[0]][j.split()[1]],tabulka[i.split()[1]][j.split()[0]]*tabulka[i.split()[1]][j.split()[1]])
        elif len(i.split())==1 and len(j.split())==2:
            moja_sila += tabulka[i][j.split()[0]]* tabulka[i][j.split()[1]]
        elif len(i.split())==2 and len(j.split())==1:
            moja_sila += max(tabulka[i.split()[1]][j], tabulka[i.split()[0]][j])
        elif len(i.split())==1 and len(j.split())==1:
            moja_sila += tabulka[i][j]

for i in nepriatelia:
    for j in moji_pokemoni:
        if len(i.split())==2 and len(j.split())==2:
            nepritelska_sila+= max(tabulka[i.split()[0]][j.split()[0]]*tabulka[i.split()[0]][j.split()[1]],tabulka[i.split()[1]][j.split()[0]]*tabulka[i.split()[1]][j.split()[1]])
        elif len(i.split())==1 and len(j.split())==2:
            nepritelska_sila += tabulka[i][j.split()[0]]* tabulka[i][j.split()[1]]
        elif len(i.split())==2 and len(j.split())==1:
            nepritelska_sila += max(tabulka[i.split()[1]][j], tabulka[i.split()[0]][j])
        elif len(i.split())==1 and len(j.split())==1:
            nepritelska_sila += tabulka[i][j]

print(moja_sila)
print(nepritelska_sila)
if moja_sila==nepritelska_sila:
    print('remíza')
elif moja_sila>nepritelska_sila:
    print('vyhral som')
elif nepritelska_sila>moja_sila:
    print('vyhral nepriatel')