import gc  # Responsible for grabage collection


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insertat(self, prev_node, new_data):
        if prev_node is None:
            print("Prev node is None! ")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def addAtLast(self, new_data):
        new_node = Node(new_data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def printDoublyLL(self, node=None):
        if node is None:
            node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.next

    def deleteDlist(self, key):
        """
        3 Cases :
        1. key is at the HEAD
        2. key is at the END
        3. key is in between.
        """
        if self.head or key is None:
            print("Key is None or self.head is None")

        # Case 1 ... here key is your object
        if self.head == key:
            self.head = key.next
            # Now after the above step the key is still hanging somewhere in the memory space!

        # Case 2 : key is somewhere in between.
        if key.next is not None:
            # 1 value forward should point to now behind value ... so we are removing the middle key node
            key.next.prev = key.prev

        # Case 3 : key is at the end
        if key.prev is not None:
            # key of previous and its next values.
            key.prev.next = key.next
        # Possible other cases

        gc.collect()  # reference of the key will be removed now







if __name__ == '__main__':
    dl = DoublyLinkedList()
    dl.push(55)
    dl.push(99)
    dl.push(698)
    dl.push(741)
    dl.push("abhishek")  # Latest value inserted will be at the top of DLL
    dl.printDoublyLL()















