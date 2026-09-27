# leetcode 1480 
# Running sum of iD array 
def sum(nums):
    for i in range(1,len(nums)):
        nums[i]=nums[i]+nums[i-1]
    return nums
nums=[1,2,3,4]
print(sum(nums))
