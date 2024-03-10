class Solution:
    def sortArray(self, nums):
        # quick sort
        def patition(nums, s, e):
            pivot = nums[e-1]
            p = s
            for i in range(s, e):
                if nums[i] < pivot:
                    # swap i and p
                    temp = nums[p]
                    nums[p] = nums[i]
                    nums[i] = temp
                    p += 1
            # swap pivot and point p
            nums[e-1] = nums[p]
            nums[p] = pivot
            return p
        
        def quickSort(nums, s, e):
            if e - s <= 1:
                return 
            pos = patition(nums, s, e)
            quickSort(nums, s, pos)
            quickSort(nums, pos+1, e)
            return nums
        
        return quickSort(nums, 0, len(nums))

        



# Test cases
solution = Solution()
print(solution.sortArray([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Expected: [1, 1, 2, 3, 4, 5, 5, 6, 9]
print(solution.sortArray([5, 4, 3, 2, 1]))           # Expected: [1, 2, 3, 4, 5]
print(solution.sortArray([1, 2, 3, 4, 5]))           # Expected: [1, 2, 3, 4, 5]