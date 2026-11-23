class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum, local_sum = nums[0], nums[0]
        l, r = 0, 0

        if len(nums) < 1:
            return maximum

        for index in range(1, len(nums)):
            local_sum += nums[index]

            while local_sum <= 0 and l <= r:
                local_sum -= nums[l]
                l += 1
            
            if local_sum > maximum:
                maximum = local_sum

            r += 1


        return maximum

        