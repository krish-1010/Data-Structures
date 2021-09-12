class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

head = None #reference to the first node

def insertAtBeginning(data):
    global head
    if head == None:
        head = Node(data)

    else:
        newnode = Node(data)
        newnode.next = head
        head = newnode

def insertAtEnd(data):
    global head
    if head == None:
        head = Node(data)

    else:
        current = head
        newNode = Node(data)
        while current.next is not None:
            current = current.next

        current.next = newNode


def insertAtMiddleAfterTarget(data,target):
    global head
    if head == None:
        head = Node(data)
    

    else:
        current = head
        
        while current != None and current.data != target:
            current = current.next
        
        if current == None:
            print("target not found")
        else:
            newnode = Node(data)
            newnode.next = current.next
            current.next = newnode

def insertAtMiddleBeforeTarget(data,target):
    global head
    if head == None:
        head = Node(data)

    else:
        if head.data == target:
            newnode = Node(data)
            newnode.next = head
            head = newnode

        else:
            current = head
            precurrent = head

            while current != None and current.data != target:
                precurrent = current
                current = current.next

            if current is None:
                print("target not found")

            else:
                newnode = Node(data)
                newnode.next = current
                precurrent.next = newnode

def deleteAtbeginning():
    global head
    if head is None:
        print('List is empty')

    else:
        current = head
        head = current.next
        del current

def deleteAtEnd():
    if head is None:
        print("List is empty")

    else:
        current = head
        precurrent = head
        while current.next is not None:
            precurrent = current
            current = current.next
        precurrent.next = None
        del current

def delete(target):
    global head
    if head is None:
        print("list is empty")

    else:
        current = head
        if target == head.data:
            head = head.next
        else:
            while current is not None and target != current.next.data:
                current = current.next

            if current is None:
                print("Target not found")
            current.next = current.next.next


def display():
    global head
    if head == None:
        print('List is empty')

    else:
        current = head
        while current is not None:
            print(current.data)
            current = current.next


# insertAtBeginning(5)
# insertAtBeginning(4)
# insertAtBeginning(3)
# insertAtMiddleBeforeTarget(100,3)
# insertAtBeginning(2)
# insertAtBeginning(1)
# insertAtBeginning(0)
# delete(100)
# insertAtEnd(101)
# deleteAtEnd()
# deleteAtbeginning()
# insertAtMiddleAfterTarget(1000,5)
# deleteAtEnd()
# display()