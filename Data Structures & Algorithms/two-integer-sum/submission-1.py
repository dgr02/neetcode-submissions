class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            index1 = nums.index(i)
            for j in nums[index1 + 1:]:
                if i + j == target:
                    index2 = nums.index(j, index1 + 1)
                    return [index1, index2]