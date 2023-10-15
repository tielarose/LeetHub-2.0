class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind_to_replace = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[ind_to_replace] = nums[i]
                ind_to_replace += 1

        return ind_to_replace

        