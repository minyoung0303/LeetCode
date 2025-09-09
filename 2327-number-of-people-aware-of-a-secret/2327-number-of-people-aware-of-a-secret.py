class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        dp[1] = 1

        for day in range(1, n + 1):
            for share_day in range(day + delay, min(n + 1, day + forget)):
                dp[share_day] = (dp[share_day] + dp[day]) % MOD

        ans = 0
        for day in range(n - forget + 1, n + 1):
            ans = (ans + dp[day]) % MOD
        
        return ans