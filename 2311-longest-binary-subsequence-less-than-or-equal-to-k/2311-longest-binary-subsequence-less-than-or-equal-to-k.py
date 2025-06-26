class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = int(s)
        s1 = ''
        
        while(n != 0 and (s1 == '' or int(s1[::-1], 2) <= k)):
            f = n % 10
            if(int((s1 + str(f))[::-1], 2) > k):
                break
            s1 += str(f)
            n //= 10

        s1 = s1[::-1]
        s2 = s[:len(s)-len(s1)]
        c = s2.count('0')

        return len('0'*c + s1)