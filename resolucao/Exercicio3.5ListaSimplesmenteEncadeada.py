class item:

    def __init__(self, data):
        self.data = data
        self.next = None

class listaSimplesmenteEncadeada:

    def __init__(self):
        self.size = 0
        self.head = None

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def addItemBack(self, data):
        new_item = item(data)
        if(self.size == 0):
            self.head = new_item
        else:
            tempItem = self.head
            while tempItem.next != None:
                tempItem = tempItem.next
            tempItem.next = new_item
        self.size += 1

    def addItemFront(self, data):
        new_item = item(data)
        if(self.size == 0):
            self.head = new_item
        else:
            tempItem = self.head
            self.head = new_item
            new_item.next = tempItem
            self.size += 1

    def removeItemBack(self):
        if(self.size == 0):
            return 
        else:
            tempItem = self.head
            tempItemB = tempItem
            while tempItem.next != None:
                tempItemB = tempItem
                tempItem = tempItem.next
            tempItemB.next = None
            self.size -= 1
            if(self.size == 0):
                self.head = None

    def removeItemFront(self):
        if(self.size == 0):
            return
        else:
            self.head = self.head.next
            self.size -= 1
            if(self.size == 0):
                self.head = None

    def printList(self):
        if(self.head != None):  
            tempItem = self.head
            while tempItem.next != None:
                print(tempItem.data)
                tempItem = tempItem.next
            print(tempItem.data)
        print(f"Tamanho: {self.size}")
            

listItem = listaSimplesmenteEncadeada()
listItem.addItemBack(2)
listItem.addItemFront(1)
listItem.addItemFront(0)
listItem.addItemBack(3)
listItem.removeItemFront()
listItem.removeItemBack()
listItem.printList()

