class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def addAtBegin(self, data):
        new_item = Node(data)
        if self.head is not None:
            self.head.prev = new_item
            new_item.next = self.head
        self.head = new_item
    
    def addAtEnd(self, data):
        new_item = Node(data)
        if self.head is not None:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = new_item
            new_item.prev = current
        else:
            self.head = new_item

    def addAtMiddle(self, data, key):
        current = self.head
        while (current.data != key) and (current != None):
            current = current.next
        if current is not None:
            new_item = Node(data)
            current.next.prev = new_item
            new_item.next = current.next
            new_item.prev = current
            current.next = new_item
        else:
            print("Number is not found")


    def deleteFirstNode(self):
        if self.head is None:
            print("The list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def deleteLastNode(self):
        if self.head is None:
            print("List is empty!")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while (current.next.next != None):
                current = current.next
            current.next = None

    def deleteAnyNode(self, value):
        if self.head is None:
            print("The list is empty!")
        elif self.head.data == value:
            self.head = self.head.next
            self.head.prev = None
        else:
            current = self.head
            while (current.next != None) and (current.next.data != value):
                current = current.next
            if current.next is not None:
                current.next.next.prev = current
                current.next = current.next.next
            else:
                print("Value not Found!")
    
    def display(self):
        current = self.head
        while(current):
            print(current.data, end=" <-> ")
            current = current.next
        print(f"None")
            







    # def delete_first(self):
    #     if self.head==None:
    #         print("list is empty")
    #     elif self.head.next==None:
    #         self.head=None
    #     else:
    #         self.head=self.head.next
    #         self.head.prev=None

    # def delete_last(self):
    #     if self.head==None:
    #         print("list is empty")
    #     elif self.head.next==None:
    #         self.head=None
    #     else:
    #         current=self.head
    #         while current.next.next:
    #             current=current.next
    #         current.next=None 
        


