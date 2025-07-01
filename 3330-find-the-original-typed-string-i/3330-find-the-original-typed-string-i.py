class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        group_list = []
        start = 0

        for i in range(1, len(word)):
            if word[i] != word[i-1]:
                group_list.append((word[i-1], i - start))
                start = i

        group_list.append((word[-1], len(word) - start))

        result = 1
        
        for char, count in group_list:
            if count >= 2:
                result += count - 1

        return result