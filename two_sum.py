# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        
        numHT = {}
        #Store all numbers that can be afiliated with the target within a hashtable so it retains index
        for i in range(len(nums)):
            if nums[i] not in numHT:
                numHT[nums[i]] = [i]
            elif nums[i]>target:
                pass
            else:
                numHT[nums[i]].append(i)
        
        #Iterate through the numbers and check if the [num] and [target - num] is in hash table
        for num in nums:
            if num in numHT:
                if target - num in numHT:
                    if target - num == num:
                        #EDGE: If it has duplicates of the same num
                        if len(numHT[num]) > 1:
                            return [numHT[num][0], numHT[num][1]]
                    else:
                        return [numHT[num][0], numHT[target - num][0]]
        return []