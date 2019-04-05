class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self,d):
        if self.value == d:              # Eru þessi gögn þegar fyrir
            return False
        elif self.value > d:             # Förum vinstra megin
            if self.left:                   # Er til leftChild
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:                               # Förum hægra megin
            if self.right:                  # Er til rightChild
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,d):
        if self.root:                       # Er til rót?
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True

    def preOrderPrint(self, root):
        # Þinn kóði hér. Endurkvæmt fall sem fer yfir í Node klasa

        if root:
            print(root.value, end=" ")

            self.preOrderPrint(root.left)

            self.preOrderPrint(root.right)


    def postOrderPrint(self, root):
        # Þinn kóði hér. Endurkvæmt fall sem fer yfir í Node klasa
        if root:
            self.preOrderPrint(root.left)

            self.preOrderPrint(root.right)

            print(root.value, end=" ")

    def delete(self, n):
        # Þinn kóði hér. Endurkvæmt fall sem fer yfir í Node klasa
        pass
    def deleteTree(self):
        del self
        pass

t = Tree()

t.insert(4)
t.insert(3)
t.insert(2)
t.insert(5)
t.insert(6)

t.preOrderPrint(t.root)
print(" ")
t.postOrderPrint(t.root)
