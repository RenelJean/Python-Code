with open("warehouse_data_final_exam_Python.txt")as f:
    lines = f.readlines()

i = 0
orderNum = []
for line in lines:
    lineHolder = lines[i]
    lineHolder = lineHolder
    orderNum.append(lineHolder)
    i += 1

i = 0

def str2int(string):
    return int(string)

pickList = []
orderList = []
for elements in orderNum:
    x = 0
    order = orderNum[i].strip('[]')
    Order = order.replace(']','').replace('\n','')
    oNum = Order.split(',')
    pickList.append(oNum)
    holderStr = pickList[i]
    hold = []
    while x < len(holderStr):
        intItems = str2int(holderStr[x])
        hold.append(intItems)
        x +=1
    orderList.append(hold)
    i += 1

pickOrder = sorted(orderList)

#Empty list holders
orderNumber = []
partNum = []
quantity = []
aisleNum = []
shelfNum = []
binNum = []
itemPickOrder = []
item = []
descript = []
productItem = []


def assignList(item):
    ctr = 0
    for element in pickOrder:
        description = pickOrder[ctr]
        orderNumber.append(description[0])
        partNum.append(description[1])
        quantity.append(description[2])
        aisleNum.append(description[3])
        shelfNum.append(description[4])
        binNum.append(description[5])
        ctr +=1
        item = [orderNumber,partNum,quantity,aisleNum,shelfNum,binNum]
        descript.append(description)
assignList(pickOrder)

