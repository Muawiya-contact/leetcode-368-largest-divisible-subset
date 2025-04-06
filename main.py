class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums:
            return []

        # Step 1: Sort the array
        nums.sort()
        n = len(nums)

        # dp[i]: length of the largest divisible subset ending with nums[i]
        dp = [1] * n

        # prev[i]: index of the previous element in the subset
        prev = [-1] * n

        max_index = 0  # index of the largest subset's last element

        # Step 2: Fill the dp array
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[max_index]:
                max_index = i

        # Step 3: Reconstruct the subset
        result = []
        i = max_index
        while i >= 0:
            result.append(nums[i])
            i = prev[i]

        return result[::-1]  # Reverse to return subset in correct order
       #By Coding Moves
