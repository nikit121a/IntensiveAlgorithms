from typing import List

class Solution:
    def countPrimes(self, n: int) -> int:
        lst = set()
        for i in range(2, n):
            lst.add(i)
        ans = 0
        for i in range(2, int(sqrt(n))+1):
            if i in lst:
                for j in range(i+1, n+1):
                    if j in lst:
                        if j % i == 0:
                            lst.remove(j)
        return len(lst)



# https://leetcode.com/problems/count-primes/
