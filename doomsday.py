def doomsday(a):

    slovnik_dni={'Sunday':0,'Monday':1,'Tuesday':2,'Wendnesday':3,'Thursday':4,'Friday':5,'Saturday':6}
    slovnik_dni_reversed = {0:'Sunday', 1:'Monday',2:'Tuesday',3: 'Wendnesday',4: 'Thursday',5: 'Friday',6: 'Saturday'}
    slovnik_kotiev = {1800:'Friday',1900:'Wendnesday',2000:'Tuesday',2100:'Sunday'}

    datum = a.split('-')
    den= int(datum[2])
    mesiac= int(datum[1])
    rok=int(datum[0])
    posledne_dve_cifry_roku = rok % 100

    if (rok % 4 == 0 and rok % 100 != 0) or (rok % 4 == 0 and rok % 400 == 0):
        kotvy_mesiacov= {1:4,2:29,3:7,4:4,5:9,6:6,7:11,8:8,9:5,10:10,11:7,12:12}
    else:
        kotvy_mesiacov = {1: 3, 2: 28, 3: 7, 4: 4, 5: 9, 6: 6, 7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12}

    kotva= slovnik_dni[slovnik_kotiev[(rok//100)*100]]
    kolko_krat_sa_smesti_12= posledne_dve_cifry_roku//12
    rozdie=posledne_dve_cifry_roku-(kolko_krat_sa_smesti_12*12)
    kolko_krat_sa_smesti_4= rozdie//4
    sucet_vsetkych=(kolko_krat_sa_smesti_12+rozdie+kolko_krat_sa_smesti_4+kotva)
    doomsday_for_year= slovnik_dni_reversed[sucet_vsetkych%7]

    for i in kotvy_mesiacov:
        if i == mesiac:
            kotevny_den = slovnik_dni[doomsday_for_year]
            rozdiel= abs(den-kotvy_mesiacov[i])
            if den > kotvy_mesiacov[i]:
                return (slovnik_dni_reversed[(kotevny_den+rozdiel)%7])
            else:
                return (slovnik_dni_reversed[(kotevny_den - rozdiel) % 7])

print(doomsday('2020-10-18'))