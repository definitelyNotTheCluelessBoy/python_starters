import sqlite3, random
conection = sqlite3.connect('C:\\sqlite\\gui\\adresy.sqlite')
database = conection.cursor()

def zjednodus()

def read_table(city,street):
    database.execute("select Latitude, Longitude from ulice, popcisla,obce where ulice.idUlice=popcisla.idUlice and ulice.IdObce=obce.idObce and obce.MenoObce like '%"+city+"%' and ulice.MenoUlice like '%"+street+"%';")
    res = database.fetchall()
    x=0.0
    y=0.0
    pointer = 0
    for i in res:
        pointer+=1
        x+= i[0]
        y+= i[1]
    averagex = x/pointer
    averagey = y/pointer
    print(averagex,averagey)
read_table('Martin','Hora')