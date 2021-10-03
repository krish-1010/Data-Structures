class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

head = None
tail = None

def push(data):
    global head
    global tail
    if head == None:
        head = Node(data)
        tail = head
    
    else:
        newnode = Node(data)
        head.next = newnode
        head = newnode

def pop():
    global head
    global tail

    if head is None:
        print('Stack is empty')

    else:
        current = tail
        while current.next is not head:
            current = current.next
        current.next = None
        head = current
        del current

def peek():
    print(head.data)

def display():
    global head
    global tail
    if head is None:
        print('Stack is empty')

    else:
        current = tail
    
        while current != None:
            print(current.data)
            current = current.next

        current = None
        del current

def isempty():
    if head is None:
        print('Yes, the stack is empty')
    else:
        print('No, the stack is not empty')



push(1)
push(2)
push(3)
push(4)
push(5)
push(0)
pop()
display()
peek()
isempty()