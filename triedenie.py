zoznamik=[7,8,1,11,8,35,6,3,5,4,11.6]

def bubblesort(mix):
    pointer = len(mix)-1
    while pointer!=0:
        if len(mix)>1:
            for i in range(0,pointer):
                if mix[i+1]<mix[i]:
                    mix[i],mix[i+1]=mix[i+1],mix[i]
        pointer -= 1
    print(mix)
bubblesort(zoznamik)

def selectionsort(mix):
    biggest = mix[0]
    pointer = len(mix)-1
    while pointer !=0:
        for i in range(0,pointer):
            if mix[i] < biggest:
                mix[i]=mix[-1]
                biggest = mix[i]
        pointer-= 1
    print(mix)
selectionsort(zoznamik)

def insertionsort(mix):
    for i in range(1,len(mix)):
        while mix[i]<mix[i-1]:
            mix[i],mix[i-1]=mix[i-1],mix[i]
            if i >1:
                i-=1
    print(mix)
insertionsort(zoznamik)