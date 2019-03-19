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

    def preOrderPrint():
        pass
        # Þinn kóði hér. Endurkvæmt fall sem fer yfir í Node klasa
        pass
    def postOrderPrint():
        # Þinn kóði hér. Endurkvæmt fall sem fer yfir í Node klasa
        pass
    def delete(n):
        # Þinn kóði hér. Endurkvæmt fall sem fer yfir í Node klasa
        pass
    def deleteTree():
        # Þinn kóði hér
        pass
t = Tree()
