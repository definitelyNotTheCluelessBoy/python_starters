import random

n= int(input('zadaj rozmer: '))

def vytvor_maticu(n):
    matica=[]
    riadok=[]
    for i in range(0,n):
        for j in range(0,n):
            riadok.append(random.randint(-10,10))
        matica.append(riadok)
        riadok=[]
    print(matica)
    return matica

matica = vytvor_maticu(n)

def MatrixAwesome(matrix):
    horna_diagonala=0
    dolna_diagonala=0
    premenna=0
    premenna2=0
    counter = 1
    counter2=0
    for i in range(len(matrix)):
        for j in range(0,len(matrix[i])-counter):
            horna_diagonala+=matrix[i][j]
            premenna+=matrix[i][j]
            print(premenna)
        for j in range(len(matrix[i])-counter2,len(matrix[i])):
            dolna_diagonala += matrix[i][-(len(matrix[i])-j)]
            premenna2 += matrix[i][-(len(matrix[i])-j)]
            print(premenna2)
        print(horna_diagonala,dolna_diagonala)
        counter +=1
        counter2+=1
        premenna=0
        premenna2=0
    if horna_diagonala==dolna_diagonala:
        return True
    else:
        return False
print(MatrixAwesome(matica))

