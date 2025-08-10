class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def signature(x):
            return ''.join(sorted(str(x)))

        power_of_two_patterns = {signature(1 << i) for i in range(31)}

        return signature(n) in power_of_two_patterns