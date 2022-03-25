class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BST:
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, key):
        """Function to decide whether to call the insert_helper or insert a HEAD node itself"""
        if self.root is None:
            self.root = key  # If the root is only None then make it as the root Node
        else:
            self.insert_helper(self.root, key)  # If root node exists then call the helper method

    def insert_helper(self, this_node, key):
        """
        This helper method is going to help us whether the value should go to left side or right side
        But if the value is to become the Node itself then it won't handle
        """
        if this_node.key > key:
            if this_node.left is None:
                this_node.left = Node(key)
            else:
                self.insert_helper(this_node.left, key)

        else:
            if this_node.right is None:
                this_node.right = Node(key)
            else:
                self.insert_helper(this_node.right, key)

    def find_inorder_successor(self, this_node):
        """We want the smallest from the right hand side"""
        myval = this_node
        while myval.left is not None:  # keep on digging the left side of the node
            myval = myval.left
        return myval

    def delete_node(self, this_node, key):
        if this_node is None:
            print("Current node is None!!")
        if key < this_node.key:
            this_node.left = self.delete_node(this_node.left, key)
        elif key > this_node.key:
            this_node.right = self.delete_node(this_node.right, key)
        else:
            # Case with no child or 1 child
            if this_node.left is None:
                temp = this_node.right
                this_node = None
                return temp
            elif this_node.right is None:
                temp = this_node.left
                this_node = None
                return temp

            # Case with 2 children
            temp = self.find_inorder_successor(this_node.right)

            this_node.key = temp.key
            this_node.right = self.delete_node(this_node.right, temp.key)

        return this_node

    # Traversing the Inorder, Preorder & Postorder of the Tree.
    def inorder(self, this_node):
        if this_node:
            self.inorder(this_node.left)
            print(this_node.key, ', ', end=" ")
            self.inorder(this_node.right)

    def preorder(self, this_node):
        if this_node:
            print(this_node.key, ", ", end=" ")
            self.preorder(this_node.left)
            self.preorder(this_node.right)

    def postorder(self, this_node):
        if this_node:
            self.postorder(this_node.left)
            self.postorder(this_node.right)
            print(this_node.key, ", ", end=" ")

