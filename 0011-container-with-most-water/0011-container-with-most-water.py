class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            curr_width = right - left
            print(right, left)
            height_r = height[right]
            height_l = height[left]
            curr_height = min(height_r, height_l)
            max_area = max(max_area, curr_width * curr_height)

            if height_r < height_l:
                right -= 1
            else:
                left += 1

        return max_area
        