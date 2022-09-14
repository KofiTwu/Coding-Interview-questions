''' 
Easy
Given an array of integers nums and an integer target, 
return the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Last completed 5/27/22
'''

nums = [2,7,11,15]
target = 9
#output (0, 1)

nums2 = [3,2,4]
target2 = 6
#output (0, 2) bear in mind that the list is sorted in the function

nums3 = [3,3]
target3 = 6
#output (1, 1)

#Time: O(NlogN)
#Space: O(1)
#the the time complexity can be improved to O(n) time and space 
#if a dictionary is used

def twoSum(array, target):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == target:
            return array[left], array[right]
        elif currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1
        else:
            return []
        
        
print(twoSum(nums, target))
    
    
#time: O(n^2)
#space: O(n)
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 print(nums[i], nums[j])
                
