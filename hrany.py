def hrany():
    file=open('C:\\Users\\PC-Matúš\\PycharmProjects\\srandypandy\\textové\\hrany.txt','r')
    for i in file:
        mesto_A = i.split(';')[0]
        mesto_B = i.split(';')[1]
        for mesto in