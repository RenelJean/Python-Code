import readFile
#six aisle
class Aisle:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return print(self.items.pop())


    def size(self):
        return len(self.items)


    def printStack(self):
        for items in reversed(self.items):
            print (items.printBin())
    
#3 shelf for each 6 aisle
class shelf:
    def __init__(self):
        self.bins = []

    def isEmpty(self):
        return self.bins == []

    def push(self,bins):
        self.bins.append(bins)

    def pop(self):
        return print(self.bins.pop())
    def __str__(self):
        return str(self.bins)

    def size(self):
        return len(self.bins)
    def printStack(self):
        for bins in reversed(self.bins):
            print(bins)
    def print_list(node):
        while node is not None:
            print(node,end = " ")
            node = node.next   
        print()


#Node class
class Bin:

    def __init__(self,item,next= None, p = None):
        self.item = item
        self.next = next
        self.prev_Item = p
    def __str__(self):
        return str(self.item)
    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next

    def get_prev(self):
        return self.prev_Item

    def set_prev(self,p):
        self.prev_Item = p

    def printBin(self):
        return print(self.item)
    def get_item(self):
        return self.item

    def set_item(self,item):
        self.item = item

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()

        print(self.item, end=" ")

#Linked list class
class Shelves:
    def __init__(self,b = None):
        self.bin = b
        self.size = 0
    def get_size (self):
        return self.size
    def add(self,item):
        #new node
        new_bin = Bin(item,self.bin)
        if self.bin:
            self.bin.set_prev(new_bin)
        self.bin = new_bin
        self.size += 1

    def remove(self,item):
        this_bin = self.bin

        while this_bin:
            if this_bin.get_item() == item:
                next = this_bin.get_next()
                prev = this_bin.get_prev()

                if next:
                    next.set_prev(prev)
                if prev:
                    prev.set_next(next)
                else:
                    self.bin = this_bin
                self.size -= 1
                return True # data returned
            else:
                this_bin = this_bin.get_next()
        return False #data not found


    def find(self,item):
        this_bin = self.bin
        while this_bin:
            if this_bin.get_item() == item:
                return item
            else:
                this_node = this_node.get_next()
        return None
            
    def print_list(node):
        while node is not None:
            print(node,end = " ")
            node = node.next   
        print("")

    def print_backward(self):
        print("[", end=" ")
        if self.bin is not None:
            self.bin.print_backward()


#add items to bin
i = 0
bin1 = Bin(1)
while readFile.binNum[i]< len(readFile.binNum):
    if readFile.binNum[i] == 1:
        bin1.next = Bin(readFile.binNum[i])
        print(bin1.next)
    i += 1
    if i == 100:
        break
aisle1 = Aisle()
shelf3 = shelf()
bin7 = Bin(readFile.pickOrder[0])
bin2 = Bin(readFile.pickOrder[1])
