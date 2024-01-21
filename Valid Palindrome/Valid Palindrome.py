class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def is_alphanumeric(char):
            return char.isalnum()

        
        cleaned_s = ''.join(filter(is_alphanumeric, s.lower()))


        return cleaned_s == cleaned_s[::-1]
