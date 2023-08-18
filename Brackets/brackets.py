from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        diction = {"]": "[", "}": "{", ")": "("}
        d = deque()
        for i in s:
            if i in diction.keys():
                if len(d) == 0:
                    return False
                if d.pop() != diction[i]:
                    return False
            else:
                d.append(i)
        if len(d) != 0:
            return False
        return True


# https://leetcode.com/problems/valid-parentheses/
