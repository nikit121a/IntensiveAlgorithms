from typing import Dict
from typing import List

import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, output, mark, q):
        curr = q.get()
        k = curr[1]
        cur = curr[0]
        mark.add(cur.val)
        if len(output) <= k:
            output.append([])
        output[k].append(cur.val)
        if cur.left is not None:
            q.put([cur.left, k+1])
        if cur.right is not None:
            q.put([cur.right,k+1])

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        mark = set()
        q = queue.Queue()
        if root is None:
            return []
        q.put([root, 0])
        while not q.empty():
            self.bfs(output, mark, q)
        return output




# https://leetcode.com/problems/binary-tree-level-order-traversal/
