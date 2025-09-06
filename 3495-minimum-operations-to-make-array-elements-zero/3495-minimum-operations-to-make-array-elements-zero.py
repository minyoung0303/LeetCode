class Solution:
    def minOperations(self, queries):
        if not queries: return 0
        max_right = max(r for _, r in queries)
        max_k = (max_right.bit_length() - 1) // 2
        starts = [1 << (2 * i) for i in range(max_k + 1)]
        prefix = [0] * (max_k + 1)
        for i in range(1, max_k + 1):
            cnt = 3 * (1 << (2 * (i - 1)))
            prefix[i] = prefix[i - 1] + cnt * i

        total = 0
        for left, right in queries:
            if right > 0:
                k = (right.bit_length() - 1) // 2
                ops_right = prefix[k] + (right - starts[k] + 1) * (k + 1)
            else:
                ops_right = 0
            a = left - 1
            if a > 0:
                k = (a.bit_length() - 1) // 2
                ops_left = prefix[k] + (a - starts[k] + 1) * (k + 1)
            else:
                ops_left = 0
            weighted = ops_right - ops_left
            total += (weighted + 1) // 2
        return total