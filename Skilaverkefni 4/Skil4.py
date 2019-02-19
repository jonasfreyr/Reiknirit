
# Skilaverkefni 4
def leita(n, l):
    for a in l:
        if a == n:
            return l.index(n)
    return -1

def insert_place(t, l):
    for index, num in reversed(list(enumerate(l))):
        if t >= num:
            l.insert(index+1, t)
            return l

    l.insert(0, t)
    return l


def binary_search(l, t, a=0, b=None):
    if b == None:
        b = len(l)

    if (a <= b):
        mid = int((a + b) / 2)

        if t == l[mid]:
            return mid

        if t > l[mid]:
            a = mid

        if t < l[mid]:
            b = mid

        return binary_search(l, t, a, b)

    return -1

class Node:
    def __init__ (self,v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self,d):
        if self.value == d: # Eru þessi gögn þegar fyrir
            return False
        elif self.value > d: # Förum vinstra megin
            if self.left: # Er til leftChild
                return self.left.insert(d)
            else:
                self.left = Node(d) # Ef ekki til nýr hnútur búinn til
                return True

        else: # Förum hægra megin
            if self.right: # Er til rightChild
                return self.right.insert(d)
            else:
                self.right = Node(d) # Ef ekki til nýr hnútur búinn til
                return True



class Tree:
    def __init__(self):
        self.root = None

    def search(self, num, node = None):
        if node is None:
            node = self.root
            if node is None:
                return False

        if num == node.value:
            return True

        if node.left is not None:
            if self.search(num, node.left) is True:
                return True

        if node.right is not None:
            if self.search(num, node.right) is True:
                return True

        return False

    def insert(self,d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True




l = [8,5,3,7,1,9,2,6]
print(l)
print("Hvaða tölu langar þér að leita? - Linear Search")
i = int(input(">> "))
print(leita(i, l))

l = [10, 14, 19, 26, 27, 31, 33, 35, 42 ,44]
print(l)
print("Hvaða tölu langar þér að leita? - Binary Search")
i = int(input(">> "))
print(binary_search(l, i))

l = [2,3,3,5,6,7,9,10]
print(l)
print("Hvaða tölu langar þér að bæta við?")
t = int(input(">> "))
l = insert_place(t,l)
print(l)

t = Tree()
t.insert(6)
t.insert(2)
t.insert(3)
t.insert(7)

print("Hvaða nótu langar þér að leita af?")
tala = int(input(">> "))
print(t.search(tala))
