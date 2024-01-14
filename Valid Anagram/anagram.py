class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
    
        countS , countT = {}, {}

        for c in s:
            countS[c] = countS.get(c,0) + 1
        for c in t:
            countT[c] = countT.get(c,0) + 1

        return countS == countT

#return Counter(s) == Counter(t) DSA

#return sorted(s) == sorted(t)