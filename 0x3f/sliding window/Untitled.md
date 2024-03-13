[1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

自己写用dfs超时了

```py
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        minop = len(nums)

        def dfs(left, right, x, op):
            nonlocal minop
            if x == 0:
                minop = min(minop, op)
                return minop
            if x < 0:
                return float('inf')
            if left >= right:
                return float('inf')
            
            op += 1
            opleft = dfs(left+1, right, x-nums[left], op)
            opright = dfs(left, right-1, x-nums[right], op)

            minop = min(minop, opleft, opright)
            return minop

        
        dfs(0, len(nums)-1, x, 0)
        
        return minop if minop != len(nums) or sum(nums) == x else -1
            
```

