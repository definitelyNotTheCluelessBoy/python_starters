import sqlite3, random

def vpisuj_do_tabulky():
    pointer=1
    zdroj = open('C:\\Users\\PC-Matúš\\PycharmProjects\\srandypandy\\textove\\15262453-4a0f-4cce-a9e4-7709e135e4b8.csv','r', encoding="utf-8")
    conection = sqlite3.connect('C:\\sqlite\\gui\\mesta.db')
    database = conection.cursor()
    for a in zdroj:
        i= a.split(',')
        database.execute("INSERT INTO mesta_obce VALUES("+str(pointer)+",'"+i[3]+"',"+str(i[4])+","+str(5)+",'"+i[6]+"','"+i[7]+"','"+i[8]+"','"+i[9]+"','"+i[10]+"','"+i[11]+"','"+i[12]+"',"+str(i[13])+",'"+i[14]+"')")
        conection.commit()
        pointer+=1
        if pointer == 2967:
            break
vpisuj_do_tabulky()