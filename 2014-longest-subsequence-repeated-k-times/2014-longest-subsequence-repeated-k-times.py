from collections import Counter, deque
from itertools import product

class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def is_valid(sub):
            target = sub * k
            j = 0
            for ch in s:
                if ch == target[j]:
                    j += 1
                    if j == len(target):
                        return True
            return False

        freq = Counter(s)
        valid_chars = [ch for ch in sorted(freq.keys(), reverse=True) if freq[ch] >= k]

        queue = deque([''])
        res = ''

        while queue:
            curr = queue.popleft()
            for ch in valid_chars:
                next_seq = curr + ch
                if is_valid(next_seq):
                    queue.append(next_seq)
                    if len(next_seq) > len(res) or (len(next_seq) == len(res) and next_seq > res):
                        res = next_seq
        return res