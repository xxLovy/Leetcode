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
L = 0

for R, x in enumerate(nums):
    if ...:
      R -= 1
    else:
...

```

## Two Pointers

### LinkedList Pointers

Core code for reverse

                nxt = cur.next
                cur.next = last
                last = cur
                cur = nxt

### Fast & Slow pointers



### Left & Right pointers

Normally it's concerned about some sum up and used for a sorted array.





## BFS

```py
queue = deque()
queue.append(root)

layer = 1
while queue:
		# layer by layer
    for _ in range(len(queue)):
      	cur = queue.popleft()
        if cur.left:
          	queue.append(cur.left)
        if cur.right:
          	queue.append(cur.right)
    print(f'layer: {layer}')
    layer += 1
```



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

## Binary Search

```py
# lower_bound 返回最小的满足 nums[i] >= target 的 i
# 如果数组为空，或者所有数都 < target，则返回 len(nums)
# 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]

# 闭区间写法
def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right+1] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1  # 范围缩小到 [left, mid-1]
    return left

# 左闭右开区间写法
def lower_bound2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)  # 左闭右开区间 [left, right)
    while left < right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right)
        else:
            right = mid  # 范围缩小到 [left, mid)
    return left  # 返回 left 还是 right 都行，因为循环结束后 left == right

# 开区间写法
def lower_bound3(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        # 循环不变量：
        # nums[left] < target
        # nums[right] >= target
        if nums[mid] < target:
            left = mid  # 范围缩小到 (mid, right)
        else:
            right = mid  # 范围缩小到 (left, mid)
    return right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums, target)  # 选择其中一种写法即可
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        # 如果 start 存在，那么 end 必定存在
        end = lower_bound(nums, target + 1) - 1
        return [start, end]
```

以下写法会返回第一个大于等于target的元素。

```py 
def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right+1] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1  # 范围缩小到 [left, mid-1]
    return left
```

