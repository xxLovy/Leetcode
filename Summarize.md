## Sort

[912. Sort an Array](https://leetcode.com/problems/sort-an-array/)

### Insertion sort

every time we assume `nums[:i]` is sorted and compare `nums[i]` with the sorted array.

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # insertion sort
        for i in range(1, len(nums)):
            # start with assuming nums[:1] is sorted
            if nums[i] < nums[i-1]:
                for j in range(len(nums[:i])-1, -1, -1):
                    # if nums[i] is smaller than the previous element, swap them
                    if nums[j+1] < nums[j]:
                        temp = nums[j]
                        nums[j] = nums[j+1]
                        nums[j+1] = temp
        return nums
```



### Merge Sort

Divide -> Conquer -> Merge

```py
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        # divide -> conquer -> merge
        def merge(left, right):
            p = q = 0
            newArray = []
            # conquer
            while p < len(left) and q < len(right):
                if left[p] > right[q]:
                    newArray.append(right[q])
                    q += 1
                elif left[p] <= right[q]:
                    newArray.append(left[p])
                    p += 1

            remainArray = left[p:] if p != len(left) else right[q:]
            newArray.extend(remainArray)
            return newArray

        def mergeSort(nums):
            # divide
            LEN = len(nums)
            if LEN <= 1:
                return nums
            half = LEN//2
            left = mergeSort(nums[:half])
            right = mergeSort(nums[half:])

            # merge
            mergedArray = merge(left, right)
            return mergedArray
        
        return mergeSort(nums)
```



### Quick Sort

Limitation:

+ only used the last element as pivot

```py
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
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
                return nums
            pos = patition(nums, s, e)
            quickSort(nums, s, pos)
            quickSort(nums, pos+1, e)
            return nums
        
        return quickSort(nums, 0, len(nums))
```



## Sliding windows

Two nested loops

```py
left = 0
right = 0

while (left < right and right < len(nums)) {
    # increase the window size
    window.append(nums[right]);
    right++;
    
    while (window needs shrink) {
        # decrease the window size
        window.remove(nums[left]);
        left++;
    }
}
```

## Two Pointers

### Fast & Slow pointers



### Left & Right pointers





## BFS



## DFS



## Backtracking

some template

```
Pick a starting point.

while(Problem is not solved)
    For each path from the starting point.
        check if selected path is safe, if yes select it
        and make recursive call to rest of the problem
        before which undo the current move.
    End For

If none of the move works out, return false, NO SOLUTON.
```

## 