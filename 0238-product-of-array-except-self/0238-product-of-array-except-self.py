class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]

        # make result a list of left-products
        for i in range(len(nums) - 1):
            result.append(result[-1] * nums[i])

        # loop again, multiplying the right product
        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result

            