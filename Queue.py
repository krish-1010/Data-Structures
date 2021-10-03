class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = None
tail = None

def enqueue(data):
    global head
    global tail
    if head is None:
        head = Node(data)
        tail = head
    
    else:
        
        newnode = Node(data)
        tail.next = newnode
        tail = tail.next

def dequeue():
    global head
    global tail
    if head is None:
        print('Queue is empty')
        
    else:
        if head.next == None:
            head = tail = None

        else:
            head = head.next

def peek():
    print(head.data)

def isempty():
    if head is None:
        print('Yes, the Queue is empty')

    else:
        print('No, the Queue is not empty')

def display():
    global head
    if head is None:
        print('Queue is empty')

    else:
        current = head
        while current != None:
            print(current.data)
            current = current.next
        current = None
        del current

enqueue(0)
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
dequeue()
display()
peek()
isempty()