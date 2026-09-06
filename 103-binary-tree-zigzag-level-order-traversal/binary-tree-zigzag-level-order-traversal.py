# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]


        """
        if root is None:
            return []

        qeue = deque()
        qeue.append(root)
        ans = []
        flag = 0

        while qeue:
            temp_list = []

            for i in range(len(qeue)):
                e = qeue.popleft()
                temp_list.append(e.val)
                if e.left !=None:
                    qeue.append(e.left)
                if e.right != None:
                    qeue.append(e.right)

            if flag ==0:
                flag =1
                ans.append(temp_list)
            else:
                flag =0
                ans.append(temp_list[::-1])
        return ans
            
                

        


        
        