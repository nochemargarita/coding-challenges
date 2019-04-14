class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        left_height = 0
        right_height = 0
        curr_left = root
        curr_right = root
        while curr_left.left or curr_right.right:
            if curr_left.left:
                left_height += 1
                curr_left = curr_left.left
            
            elif curr_right.right:
                right_height += 1
                curr_right = curr_right.right
        
        return max(left_height, right_height)

T=[20,50,35,44,9,15,62,11,13]
myTree=Solution()
root=None
for data in T:
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height