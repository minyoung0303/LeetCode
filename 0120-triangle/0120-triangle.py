class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = triangle[-1]

        for row in range(len(triangle) - 2, -1, -1):
            new_dp = []
            for i in range(len(triangle[row])):
                new_dp.append(triangle[row][i] + min(dp[i], dp[i+1]))
            dp = new_dp

        return dp[0]