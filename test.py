from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = [0]*len(spells)
        potions.sort()
        for i in range(len(spells)):
            if spells[i] * potions[-1] < success:
                continue
            if spells[i] * potions[0] >= success:
                ans[i] = len(potions)
                continue
            else:
                # binary search: find the first element that is larger
                L = 0
                R = len(spells) - 1
                while R >= L:
                    M = (L + R) // 2
                    if spells[i] * potions[M] <= success:
                        L = M+1
                    elif spells[i] * potions[M] > success:
                        R = M-1
                print(len(potions))
                print(M)
                ans[i] = len(potions) - M
                    
        return ans

# Example usage:
solution = Solution()
print(solution.successfulPairs([5,1,3], [1,2,3,4,5], 7))
