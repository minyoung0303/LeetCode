class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        mod = 10**9 + 7

        powers = []
        for i in range(64):
            if (n >> i) & 1:
                powers.append(1 << i)
        
        prefix = [1]
        for p in powers:
            prefix.append((prefix[-1] * p) % mod)

        def modinv(x):
            return pow(x, mod-2, mod)

        ans = []
        for l, r in queries:
            val = (prefix[r+1] * modinv(prefix[l])) % mod
            ans.append(val)
        
        return ans