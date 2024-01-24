class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                total_sum = a + nums[l] + nums[r]

                if total_sum > 0:
                    r -= 1
                elif total_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res
