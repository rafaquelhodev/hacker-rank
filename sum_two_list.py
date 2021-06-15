def twoSum(nums, target):
    # nums.sort()
    for i in range(0,len(nums)):
        for j in range(0, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))