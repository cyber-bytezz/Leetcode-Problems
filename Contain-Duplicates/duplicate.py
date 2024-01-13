class Solution(object):
    def containsDuplicate(self, nums):
        num = set()                   #Declaring The Set Of Numbers
        for n in nums:                #Checking The Range
            if n in num:              #Giving Condition For True or False
                return True            
            num.add(n)                #Matching One By One
        return False
