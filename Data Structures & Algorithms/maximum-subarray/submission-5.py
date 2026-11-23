class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum, local_sum = nums[0], 0
        
        for num in nums:
            if local_sum < 0:
                local_sum = 0

            local_sum += num
            maximum = max(local_sum, maximum)

        return maximum

        