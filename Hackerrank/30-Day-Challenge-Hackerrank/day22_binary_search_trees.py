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
        left_counter = 0
        right_counter = 0
        if root is not None:
            if root.left is not None:
                left_counter = 1 + self.getHeight(root.left)
            if root.right is not None:
                right_counter = 1 + self.getHeight(root.right)
            
        return max(left_counter, right_counter)

sample_1 = [20,50,35,44,9,15,62,11,13] # 4
sample_2 = [25,39,12,19,9,23,55,31,60,35,41,70,90] # 5
sample_3 = [3,5,2,1,4,6,7] # 3

myTree=Solution()
root=None
for data in sample_3:
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height