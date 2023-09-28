import sqlite3, random
conection = sqlite3.connect('C:\\sqlite\\gui\\moja_prva')
database = conection.cursor()

def create_name():
    word = ''
    vowels= 'aeiouy'
    consonants = 'qwrtpsdfghjklzxcvbnm'
    for i in range(0,random.randint(6,10)):
        if i == 0:
            word+= (vowels+consonants)[random.randint(0,len(vowels+consonants)-1)].upper()
        else:
            if word[i-1].lower() in vowels:
                word+= consonants[random.randint(0,len(consonants)-1)]
            else:
                word+= vowels[random.randint(0,len(vowels)-1)]
    return word

def fill_table():
    for i in range(1,1001):
        database.execute("INSERT INTO ziaci (meno,priezvisko,vek,farba_oci) VALUES('"+create_name()+"','"+create_name()+"',"+str(random.randint(14,17))+","+str(random.randint(1,4))+")")
        conection.commit()
#fill_table() #"+str(i)+",'
def read_table():
    database.execute("select t1,*,t2,* from ziaci as t1, oci as t2 where t1,farba_oci = t2, id")
    res = database.fetchall()
    for i in res:
        print(i[1])
read_table()