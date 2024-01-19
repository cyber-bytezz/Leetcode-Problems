class Solution(object):
    def twoSum(self, nums, target):
        number = {}

        for i , num in enumerate(nums):
            diff = target - num

            if diff in number:
                return[number[diff], i]
            number[num] = i
        return[]
