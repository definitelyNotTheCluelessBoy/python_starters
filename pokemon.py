import pandas as pd, json
prefile = open('C:\\Users\\PC-Matúš\\PycharmProjects\\srandypandy\\textove\\pokemon.txt', 'r')
file=prefile.read()
pokemon = json.loads(file)

print(pokemon)
result = {}
subresult={}

for i in pokemon:
    for j in pokemon[i]:
        #print(j)
        for k in pokemon[i][j]:
            if i == 'super effective':
                subresult[k]=2.0
            elif i == 'normal effective':
                subresult[k] = 1.0
            elif i == 'not very effective':
                subresult[k] = 0.5
            elif i == 'no effect':
                subresult[k] = 0
        #print(subresult)
        if i == 'super effective':
            result[j]=subresult
        else:
            result[j]={**result[j],**subresult}
        subresult={}
print(result)

#print(pokemon)
#isinstance(a[i],dict)
