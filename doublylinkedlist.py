class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

head = None
tail = None

def insertAtBeginning(data):
    global head
    global tail
    if head is None:
        head = Node(data)
        tail = head
    else:
        newnode = Node(data)
        newnode.next = head
        head.prev = newnode
        head = newnode
        del newnode

def insertAfterTarget(data,target):
    global head
    global tail
    if head is None:
        while True:
            print('target not found')
            a = input("do you want to add this as a first node? (y/n)")
            if a == 'y' or 'Y':
                head = Node(data)
                tail = head
            else:
                return
    else:
        
        if head.data == target:
            if head.next == None:
                        head.next = Node(data)
                        tail = head.next
                        tail.prev = head

            elif head.next == tail:
                newnode = Node(data)
                newnode.next = tail
                newnode.prev = head
                head.next = newnode
                tail.prev = newnode
                del newnode

            else:
                newnode = Node(data)
                newnode.prev = head
                newnode.next = head.next
                head.next.prev = newnode
                head.next = newnode

        elif tail.data == target:
            newnode = Node(data)
            tail.next = newnode
            newnode.prev = tail
            tail = newnode
            del newnode

        else:
            hcurrent = head.next
            tcurrent = tail.prev
            if tcurrent == target:
                newnode = Node(data)
                newnode.next = tail
                newnode.prev = tcurrent
                tcurrent.next = newnode
                tail.prev = newnode
            else:
                while hcurrent.data != target and tcurrent.data != data:
                    hcurrent = hcurrent.next
                    tcurrent = tcurrent.prev
                if ((hcurrent == tcurrent) and (hcurrent.data and tcurrent.data != target)):
                    print('target not found')
                    return
                elif hcurrent.data == target:
                    newnode = Node(data)
                    newnode.prev = hcurrent
                    newnode.next = hcurrent.next
                    hcurrent.next.prev = newnode
                    hcurrent.next = newnode
                    
                elif tcurrent.data == target:
                    newnode = Node(data)
                    newnode.prev = tcurrent
                    newnode.next = tcurrent.next
                    tcurrent.next.prev = newnode
                    tcurrent.next = newnode

def insertBeforeTarget(data,target):
    pass

def insertAtEnd(data):
    global head
    global tail
    if head is None:
        head = Node(data)

    else:
        newnode = Node(data)
        tail.next = newnode
        newnode.prev = tail
        tail = newnode
        del newnode

def deleteAtBeginning():
    global head
    global tail
    if head is None:
        print('list is empty')

    else:
        head = head.next
        head.prev = None

def delete(data):
    global head
    global tail
    if head is None:
        print('list is empty')
    
    else:
        if data == head.data and head.next == None:
            head = None

        elif data == head.data and head.next == tail:
            head = head.next
            head.prev = None
            tail.prev = None

        elif data == head.next.data:
            head.next = tail
            tail.prev = head

        elif data == head.data:
            head = head.next
            head.prev = None

        elif data == tail.data:
            tail = tail.prev
            tail.next = None

        elif data == tail.prev.data:
            current = tail.prev
            tail.prev.prev.next = tail
            tail.prev = tail.prev.prev
            current.next = None
            current.prev = None
            del current

        else:
            current = head.next
            while current.data != data:
                current = current.next
        
            current.prev.next = current.next
            current.next.prev = current.prev
            del current
            
def deleteAtEnd():
    global head
    global tail
    if head is None:
        print('list is empty')

    else:
        tail = tail.prev
        tail.next = None

def display():
    if head is None:
        print("list is empty")

    else:
        current = head
        while current is not None:
            print(current.data)
            current = current.next
        del current

insertAtBeginning(4)
insertAtBeginning(3)
insertAtBeginning(2)
insertAtBeginning(100)
insertAtBeginning(1)
insertAtEnd(5)
insertAtEnd(6)
deleteAtEnd()
insertAtBeginning(0)
deleteAtBeginning()
delete(100)
display()
# print(head.data,head.next.data,head.next.next.data,head.next.next.next.data,head.next.next.next.next.data)
# print(tail.data,tail.prev.data,tail.prev.prev.data,tail.prev.prev.prev.data,tail.prev.prev.prev.prev.data)