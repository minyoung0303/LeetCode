class Solution(object):
    def possibleStringCount(self, word, k):
        MOD = 10**9 + 7

        # 1) Run‐length encode word into runs r[i]
        r = []
        prev = None
        for ch in word:
            if ch == prev:
                r[-1] += 1
            else:
                r.append(1)
                prev = ch
        m = len(r)

        total = 1
        for ri in r:
            total = total * ri % MOD

        if m >= k:
            return total

        S = k - m

        dp = [0] * S
        dp[0] = 1

        for ri in r:
            ci = ri - 1

            ps = [0] * (S + 1)
            for j in range(S):
                ps[j+1] = (ps[j] + dp[j]) % MOD

            new = [0] * S
            for j in range(S):

                low = j - ci
                if low <= 0:

                    new[j] = ps[j+1]
                else:

                    new[j] = (ps[j+1] - ps[low]) % MOD
            dp = new

        bad = sum(dp) % MOD
        return (total - bad) % MOD