class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}  
    
        for c in strs:
            sort = ''.join(sorted(c))  
            if sort in anagrams:
                anagrams[sort].append(c) 
            else:
                anagrams[sort] = [c]  

        result = list(anagrams.values())  

        return result  
