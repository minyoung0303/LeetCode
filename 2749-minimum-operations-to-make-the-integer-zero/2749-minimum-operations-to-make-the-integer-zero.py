class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        for k in range(1, 61):
            val = num1 - k * num2
            if val < k:
                continue
            if bin(val).count("1") <= k:
                return k
        return -1