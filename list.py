class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def printList(self):
        current = self.head

        while current:
            print(f"{current.data} -> ")
            current = current.next

    def hasCycle(self):
     slow = self.head
     fast = self.head

     while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("Cycle found...")
            return True
     print("No cycle found.")
     return False


lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)

first = lst.head
second = first.next
third = second.next
fourth = third.next

fourth.next = second

lst.hasCycle()