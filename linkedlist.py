class MyNode:
    def __init__(self, value):
        self.data = value
        self.nextPointer = None

class MyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def printmyLinkedList(self):
        temp = self.head
        while(temp != None):
            print(temp.data, "->", end ="")
            temp = temp.nextPointer
        print("None\n")

    def insert(self, val):
        newNode = MyNode(val)
        if(self.head == None):
            self.head = newNode
            return
        temp=self.head
        while(temp.nextPointer != None):
            temp= temp.nextPointer
        temp.nextPointer= newNode

    def delete(self, val):
        temp=self.head
        prev= temp
        while(temp !=None and temp.data !=val):
            prev = temp
            temp=temp.nextPointer
        if(temp != None):
            prev.nextPointer=temp.nextPointer
        pass

    def search(self, param):
        temp=self.head
        ret =0
        while(temp !=None):
            if(temp.data ==param):
                ret= 1
                break
            temp=temp.nextPointer
        if(ret==1):
            print('Yes')
        else:
            print('No')

    def getSize(self):
        count=0
        temp=self.head
        while(temp != None):
            count+=1
            temp=temp.nextPointer
        return count

    def getElementAtPos(self, index):
        count=1
        temp=self.head
        while(temp != None and count<index):
            count+=1
            temp=temp.nextPointer
        return temp.data

    def deleteFirstNode(self):
        self.head=self.head.nextPointer
        pass


mylist = MyLinkedList()
# mySecList= MyLinkedList()
mylist.printmyLinkedList()
# mySecList.insert(7777)
# mySecList.printmyLinkedList()
mylist.insert(12)
mylist.printmyLinkedList()
mylist.insert(17)
mylist.printmyLinkedList()
mylist.insert(65)
mylist.insert(85)
mylist.insert(1122)
mylist.printmyLinkedList()
# mylist.delete(85)
# mylist.printmyLinkedList()
mylist.search(17)
print(mylist.getSize())
mylist.insert(102)
print(mylist.getSize())
mylist.printmyLinkedList()
print(mylist.getElementAtPos(4))
# Next task : Implement the 5 methods below :
# mylist.replaceValueAtPos(2, 99)
mylist.deleteFirstNode()
mylist.printmyLinkedList()
mylist.delete(444)
mylist.printmyLinkedList()
# mylist.deleteElementAtPos(3)
# mylist.deleteFirstItem()
# mylist.deleteLastItem()
