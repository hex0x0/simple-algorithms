
inventory = {'rope':1, 'torch': 6, 'gold coin': 42, 'dagger':1, 'arrow':12}





def displayInventory(inventory):
    totalNumber=0
    for k, v in inventory.items():
        totalNumber+=v
        print(v, k)
    
    print('Total number of items: ' + str(totalNumber))




displayInventory(inventory)