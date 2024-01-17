class Solution(object):
    def topKFrequent(self, nums, k):
        element = {}

        for n in nums:
            if n in element:
                element[n] +=1
            else:
                element[n] = 1

        result = []

        for i in range(k):
            max_num = max(element, key = element.get)
            result.append(max_num)
            del element[max_num]

        return result