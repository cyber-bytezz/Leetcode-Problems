class Solution(object):
    def productExceptSelf(self, nums):
        product = len(nums)

        output = [1]* product

        left = 1
        for i in range(product):
            output[i] *= left
            left *=nums[i]
        right = 1
        for  i in range(product-1, -1, -1,):
            output[i]*=right
            right*=nums[i]

        return output