class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        result = []
        i = 0
        while i < len(s):
            group = s[i:i + k]
            if len(group) < k:
                group += fill * (k - len(group))
            result.append(group)
            i += k
        return result