from typing import Dict
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def req1(self, root, diction):
        if root.val not in diction:
            diction[root.val] = set()
        if root.left is not None:
            diction[root.val].add(root.left.val)
            if root.left.val not in diction:
                diction[root.left.val] = set()
            diction[root.left.val].add(root.val)
            self.req1(root.left, diction)
        if root.right is not None:
            diction[root.val].add(root.right.val)
            if root.right.val not in diction:
                diction[root.right.val] = set()
            diction[root.right.val].add(root.val)
            self.req1(root.right, diction)

    def req2(self, target, k, diction, output, mark):
        if k == 0:
            output.append(target)
            return
        mark.add(target)
        for i in diction[target]:
            if i not in mark:
                self.req2(i, k - 1, diction, output, mark)
        return

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # tree = {}
        # k=-1
        # while True:
        #     if pow(2, k) > len(root)
        #         break
        #     k += 1
        diction = {}
        self.req1(root, diction)
        output = []
        mark = set()
        self.req2(target.val, k, diction, output, mark)
        output.sort(reverse=True)
        return output

# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
