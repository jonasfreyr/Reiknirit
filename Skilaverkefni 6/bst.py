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
            self.postOrderPrint(root.left)

            self.postOrderPrint(root.right)

            print(root.value, end=" ")

    def minValueNode(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, root, n, prev=0):
        if prev == 0:
            prev = root

        if root is None:
            return False

        if n < root.value:
            return self.delete(root.left, n, root)

        elif n > root.value:
            return self.delete(root.right, n, root)

        else:
            if root.left is None:
                if prev.left == root:
                    prev.left = root.right

                elif prev.right == root:
                    prev.right = root.right

                return True

            elif root.right is None:
                if prev.left == root:
                    prev.left = root.left

                elif prev.right == root:
                    prev.right = root.left

                return True

            temp = self.minValueNode(root.right)

            root.value = temp.value

            self.delete(root.right, temp.value)

        return True


    def deleteTree(self):
        self.root = None

t = Tree()

t.insert(50)
t.insert(30)
t.insert(20)
t.insert(40)
t.insert(70)
t.insert(60)
t.insert(80)


print("Pre-Order")
t.preOrderPrint(t.root)
print(" ")
print("Post-Order")
t.postOrderPrint(t.root)
print(" ")
print("Pre-Order eftir að hafa delete-að 50")
print(t.delete(t.root, 50))
t.preOrderPrint(t.root)
print(" ")
print("Reyni að delete-a 100(er ekki til)")
print(t.delete(t.root, 100))
t.preOrderPrint(t.root)
