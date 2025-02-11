print("Hello")
print("1")
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

num = int(input("Enter a number: "))
print("Factorial:", factorial_recursive(num))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

# Usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()  # Output: 10 -> 20 -> 30 -> None
ll.delete(20)
ll.display()  # Output: 10 -> 30 -> None
class HashSet:
    def __init__(self):
        self.set = {}

    def add(self, key):
        self.set[key] = True

    def remove(self, key):
        if key in self.set:
            del self.set[key]

    def contains(self, key):
        return key in self.set

    def display(self):
        print("HashSet:", list(self.set.keys()))

# Usage
hs = HashSet()
hs.add(5)
hs.add(10)
hs.add(15)
hs.display()  # Output: HashSet: [5, 10, 15]
print(hs.contains(10))  # Output: True
hs.remove(10)
print(hs.contains(10))  # Output: False
hs.display()  # Output: HashSet: [5, 15]

