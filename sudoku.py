def nacitaj(cesta):
    alpha_zoznam=[]
    subor=open(cesta,'r')
    for i in subor:
        beta_zoznam = []
        b= i.rstrip('\n').split(' ')
        for j in b:
            beta_zoznam.append(int(j))
        alpha_zoznam.append(beta_zoznam)
    return alpha_zoznam
sud=nacitaj('sudoku.txt')

def checkit(x,y,n):
    if n in sud[y]:
        return False
    for i in sud:
        if n == i[x]:
            return False
    xy_stvorca = (x//3*3,y//3*3)
    # for i in sud[xy_stvorca[0]:xy_stvorca[0]+3]:
    #      for j in i [xy_stvorca[1]:xy_stvorca[1]+3]:
    #          if j == n:
    #               return False
    for i in range(0,3):
         for j in range(0,3):
             if n == sud[i+xy_stvorca[1]][j+xy_stvorca[0]]:
                 return False
    return True

#print(checkit(0,8,4))

def dopln():
    global sud
    for i in range(0,9):
        for j in range(0,9):
            if sud[i][j]==0:
                for n in range(1,10):
                    if checkit(j,i,n):
                        sud[i][j]=n
                        dopln()
                        sud[i][j]=0
                return
    print(sud)
dopln()