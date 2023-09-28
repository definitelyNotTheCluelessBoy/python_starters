import math
A = 0.04
B = 0.0005
G = 0.2
S = 0.00005

def rabbits(n):
    if n == 0:
        return 5891
    else:
        return rabbits(n-1)+math.floor(rabbits(n-1)*(A-B*foxes(n-1)))
def foxes(n):
    if n == 0:
        return 16
    else:
        return foxes(n-1)-math.floor(foxes(n-1)*(G-S*rabbits(n-1)))

#print(rabbits(10))
#print(foxes(10))


def rabbits_and_foxes(rabbitsatstart,foxesatstart,years):
    for i in range (0,years):
        rabbitsnextyear = rabbitsatstart + math.floor(rabbitsatstart*( A - B * foxesatstart))
        foxesnextyear = foxesatstart - math.floor(foxesatstart* (G - S * rabbitsatstart))
        rabbitsatstart=rabbitsnextyear
        foxesatstart=foxesnextyear
    return rabbitsatstart,foxesatstart

print(rabbits_and_foxes(5891,16,99))