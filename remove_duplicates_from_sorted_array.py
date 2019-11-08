class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length <=1:
            return length
        stump = 0
        cur = 1
        while cur < length:
            if nums[stump] == nums[cur]:
                cur += 1
            else:
                stump += 1
                nums[stump] = nums[cur]
        return stump+1