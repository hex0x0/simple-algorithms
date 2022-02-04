import pprint
allGuests = {'alice':{'apples':5, 'pretzels': 12}, 'bob':{'ham sand': 3, 'apples':5}}

def totalBrought(guests, item):
    numBrought=0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
        
    return numBrought




print('Apples ' + str(totalBrought(allGuests, 'apples')))

print('Pretzels ' + str(totalBrought(allGuests, 'pretzels')))