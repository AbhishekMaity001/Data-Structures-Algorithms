
# Linked List Operations
class Node:
    """
    Node Class will just create a Node which contains 2 things/objects
    1. data
    2. next (pointer to the next data/value)
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Linky:
    """Linky class will be used to push, insertAt, append a new node(data + next)"""
    def __init__(self):
        self.head = None  # head variable will hold what is the latest value of the Linked List

    def push(self, new_value):
        new_node = Node(new_value)  # Creating a Node class object
        new_node.next = self.head   # Changing the new_node.next variable
        self.head = new_node  # Putting the current head info

    def insertAt(self, prev_node, new_value):
        if prev_node is None:
            print("Previous Node is empty!")
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def printlist(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next

    def deleteNode(self, key):
        temp = self.head

        # Case 1 - If the delete node itself is the current Head
        if (temp is not None):
            if (temp.data==key):
                self.head = temp.next
                temp = None
                return

        # Case 2 - If it not head
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # Case 3 - If head is None
        if temp == None:
            print("Head is None!")
            return
        prev.next = temp.next
        temp = None

    def deleteAll(self):
        curr = self.head  # going from the head
        while curr:
            prev = curr.next  # storing the next address node
            del curr.data  # deleting current node
            curr = prev  # storing next data into curr to have access what's next

    def getNodeCount(self, node):
        if not node:  # if node is None then return 0
            return 0
        else:  # until that keep on counting.
            return 1 + self.getNodeCount(node.next)

    def getCount(self):
        return self.getNodeCount(self.head)

    def reverseLinkedList(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # def printlist_rev(self):
    #     """Print the linked list in reverse order."""
    #     last = self.head
    #     while(last.next):
    #         last = last.next
    #     print(last.data)

if __name__ == '__main__':
    linked_list = Linky()

    # linked_list.append(300)
    linked_list.append(3)  # append will attach the value at the end of linked list
    linked_list.push(4)  # push will attach the value at the top
    linked_list.push(5)
    linked_list.push(6)
    # linked_list.append(33)
    # linked_list.insertAt(linked_list.head.next, 555555555)
    linked_list.deleteNode(3)
    linked_list.printlist()
