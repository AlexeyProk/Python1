

#Implement a binary search tree (BST) and include methods for inserting nodes and searching for a value.
#Instructions:
#Implement a class Node that represents a node in the BST.
#Implement a class BinarySearchTree that supports inserting nodes and searching for a value.
#Write test cases to verify the implementation.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_rec(self.root, data)

    def _insert_rec(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_rec(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_rec(node.right, data)
    def search(self, data):
        return self._search_rec(self.root, data)


    def _search_rec(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        if data < node.data:
            return self._search_rec(node.left, data)
        return self._search_rec(node.right, data)
# Lets Test it
def test_bst():
    bst = BinaryTree()
    values = [1, 5, 10, 20, 40, 65, 91]
    for v in values:
        bst.insert(v)

    assert bst.search(10) == True
    assert bst.search(1) == True
    assert bst.search(91) == True
    assert bst.search(20) == True
    assert bst.search(40) == True
    assert bst.search(20) == True
    assert bst.search(80) == False
    assert bst.search(90) == False

    print("tests GTG")

if __name__== "__main__":
    test_bst()

