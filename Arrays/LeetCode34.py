'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''

# Basicamente hay que hacer una busqueda binaria de los indices del elemento
def search(nums, target):
    l, r = 0, len(nums)-1
        
    while l < r:
        mid = (l+r)//2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            r = mid-1
        else:
            l = mid+1
    return False
    
def searchRange(nums, target):
    res = [-1, -1]
    if not nums or not search(nums, target):
        return res
        
    l, r = 0, len(nums)-1
    # We first find the left bound
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] == target:
            res[0] = mid
            r = mid - 1 # To find the left bound, because the same element could be more at left
        elif nums[mid] > target:
            r = mid-1
        else:
            l = mid + 1
                
    l, r = 0, len(nums) -1
    # Finally found the right bound
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] == target:
            res[1] = mid
            l = mid + 1 # To find the right bound, we're juat basicaly finding the last ocurrance of the target
        elif nums[mid] > target:
            r = mid-1
        else:
            l = mid + 1
    return res