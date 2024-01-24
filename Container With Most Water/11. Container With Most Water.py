class Solution(object):
    def maxArea(self, height):
        max_water = 0
        left_pointer, right_pointer = 0, len(height) - 1

        while left_pointer < right_pointer:

            width = right_pointer - left_pointer

            container_height = min(height[left_pointer], height[right_pointer])


            current_water = width * container_height
            max_water = max(max_water, current_water)


            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water

