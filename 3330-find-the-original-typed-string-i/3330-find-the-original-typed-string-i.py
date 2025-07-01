class Solution(object):
    def possibleStringCount(self, word):
        res, cnt = 1, 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                cnt += 1
            else:
                if cnt >= 2:
                    res += cnt - 1
                cnt = 1
        if cnt >= 2:
            res += cnt - 1
        return res
