"""A Node class is provided for you in the editor. A Node object has an integer
data field, data, and a Node instance pointer, next, pointing to another node
(i.e.: the next node in a list).

A Node insert function is also declared in your editor. It has two parameters: a
pointer, head, pointing to the first node of a linked list, and an integer data
value that must be added to the end of the list as a new Node object.

Task
Complete the insert function in your editor so that it creates a new Node
(pass data as the Node constructor argument) and inserts it at the tail of the
linked list referenced by the head parameter. Once the new node is added, return
the reference to the head node.

Note: If the head argument passed to the insert function is null, then the initial
list is empty.

Input Format

The insert function has 2 parameters: a pointer to a Node named head, and an
integer value, data.
The constructor for Node has 1 parameter: an integer value for the data field.

You do not need to read anything from stdin.

Output Format

Your insert function should return a reference to the head node of the linked list."""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        new_node = Node(data)
        if head is None:
            head = new_node
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node
        return head

# Input 1
# 4
# 2
# 3
# 4
# 1

# Output 1
# 2 3 4 1

# Input 2
# 5
# 8
# 11
# 2
# 3
# 4

# Output 2
# 8 11 2 3 4