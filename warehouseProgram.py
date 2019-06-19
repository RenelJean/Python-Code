import readFile
import Final

#Creates aisle
aisle1 = Final.Aisle()
aisle2 = Final.Aisle()
aisle3 = Final.Aisle()
aisle4 = Final.Aisle()
aisle5 = Final.Aisle()
aisle6 = Final.Aisle()

def ShelfLocation(shelf):
    shelf3 = Final.shelf()
    shelf2 =  Final.shelf()
    shelf1 =  Final.shelf()



#b =binLocation(readFile.binNum[0],readFile.descript[0])
#
def binLocation(binNumber,productList):
    if binNumber == 1:
        bin1 = Final.Bin(productList)
        return print(bin1)
    if binNumber == 2:
        bin2 = Final.Bin(productList)
        return print(bin2) 
    if binNumber == 3:
        bin3 = Final.Bin(productList)
        return bin3
    if binNumber == 4:
        bin4 = Final.Bin(productList)
        return bin4
    if binNumber == 5:
        bin5 = Final.Bin(productList)
        return bin5
    if binNumber == 6:
        bin6 = Final.Bin(productList)
        return bin6
    if binNumber == 7:
        bin7 = Final.Bin(productList)
        return bin7
    if binNumber == 8:
        bin8 = Final.Bin(productList)
        return bin8
    if binNumber == 9:
        bin9 = Final.Bin(productList)
        return bin9
    if binNumber == 10:
        bin10 = Final.Bin(productList)
        return bin10

print('Aisle  Shelf    Bin   Part number   Quantity  Order Number')
i = 0
for element in readFile.descript:
    item = readFile.descript[i]
    aisle = item[3]
    part = item[1]
    quantity = item[2]
    order = item[0]
    binNum = item[5]
    shelf = item[4]
    i += 1



def sortAisle(list):
    sortedList = []
    i = 0
    #sorts aisle
    for element in readFile.descript:
        product = readFile.descript[i]
        aisle = product[3]
        part = product[1]
        quantity = product[2]
        order = product[0]
        binNum = product[5]
        shelf = product[4]
        holder = [aisle,shelf,binNum,part,quantity,order]
        sortedList.append(holder)
        i += 1
    return sortedList


#sort shelf
sortedAis = []    
sortedAisle = sorted(sortAisle(readFile.descript))
holder =[]
#def sortShelf(list):
i = 0
while i < len(sortedAisle):
    product = sortedAisle[i]
    aisle = product[0]
    part = product[3]
    quantity = product[4]
    order = product[5]
    binNum = product[2]
    shelf = product[1]
    holder = [shelf,aisle,binNum,part,quantity,order]
    sortedAis.append(holder)
    i += 1
sortedShelves = []
sortedShelves = sorted(sortedAis,reverse = True)
    
sortedBin = []
i = 0
holder = []
for element in sortedShelves:
    product = sortedShelves[i]
    aisle = product[1]
    part = product[3]
    quantity = product[4]
    order = product[5]
    binNum = product[2]
    shelf = product[0]
    holder = [binNum,shelf,aisle,part,quantity,order]
    sortedBin.append(holder)
    i += 1

sortedBin = sorted(sortedBin)
    

originalFormat = []
i = 0
holder = []
for element in sortedBin:
    item = sortedBin[i]
    aisle = item[2]
    shelf = item[1]
    binNum = item[0]
    productNum = item[3]
    quantity = item[4]
    order = item[5]
    holder = [aisle,shelf,binNum,productNum,quantity,order]
    originalFormat.append(holder)
    i += 1
sortedOrigin = sorted(originalFormat)
x = 0

#print out items
for element in sortedOrigin:
    item = sortedOrigin[x]
    aisle = item[0]
    shelf = item[1]
    binNum = item[2]
    productNum = item[3]
    quantity = item[4]
    order = item[5]
    print(aisle,"    ",shelf,"     ",binNum,"      ",productNum, "      ",quantity,"     ",order)
    x += 1

