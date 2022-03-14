class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """Appending the data in circular linked list"""
        new_node = Node(new_data)
        temp = self.head  # Storing the current head separately

        new_node.next = self.head  # Since it is Circular so pushing will happend at the end only

        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node  # If head is None then make the single element next to itself.
        # Always set the head at the end of push operation in any Linked List
        self.head = new_node

    def printCircularLinkedList(self):
        temp = self.head
        if self.head is not None:
            while 1:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break

    def delete(self, delete_value):
        curr_node = self.head
        prev_node = None
        while curr_node:
            if curr_node.data == delete_value and curr_node == self.head:
                # Case 1 : If there is only 1 Node in Circular LL
                if curr_node.next == self.head:
                    curr_node = None
                    self.head = None
                    return

                # Case 2 : There are more elements in the Cllist We want to delete the head
                # Traverse and update head; delete head
                else:
                    while (curr_node.next!=self.head):
                        curr_node = curr_node.next
                    curr_node.next = self.head.next
                    self.head = self.head.next
                    curr_node = None
                    return
            elif curr_node.data == delete_value:
                prev_node.next = curr_node.next
                curr_node = None
                return
            else:
                if curr_node.next == self.head:
                    print("Data Not found for deletion!")
                    break

                prev_node = curr_node
                curr_node = curr_node.next
                curr_node = None

    def countnodes(self):
        current = self.head
        count = 0 if self.head is None else 1
        while current.next != self.head:
            count = count + 1
            current = current.next
        print("\n Total Clist count is ==> ", count)
        return

    def tocircular(self, head):
        start_fix = head
        while head.next is not None:  # Looping through the LL till the end
            head = head.next
        head = start
        return


if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.push(10)
    cll.push(99)
    cll.push(111)
    cll.push(22)
    cll.push(1)
    cll.push(44)
    cll.printCircularLinkedList()
    cll.countnodes()


