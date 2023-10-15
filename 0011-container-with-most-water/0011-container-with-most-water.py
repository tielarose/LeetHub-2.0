class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            curr_width = right - left
            max_area = max(max_area, min(height[right], height[left]) * curr_width)
            
            if height[right] == height[left]:
                right -= 1
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return max_area
        