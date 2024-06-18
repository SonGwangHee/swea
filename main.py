# SWEA 7-25
bloodtypes = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

totalDict = {}

for bloodtype in bloodtypes:
    if bloodtype in totalDict:
        totalDict[bloodtype] += 1
        print(bloodtype)
    else:
        totalDict[bloodtype] = 1

print(totalDict)

