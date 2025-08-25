class Solution:
    def findDiagonalOrder(self, mat):
        m, n = len(mat), len(mat[0])
        v = []
        flag = 0

        # Traverse diagonals starting from each row of first column
        for i in range(m):
            j, k = i, 0
            temp = []
            while j >= 0 and k < n:
                temp.append(mat[j][k])
                j -= 1
                k += 1
            if flag % 2 == 0:
                v.append(temp)
            else:
                temp.reverse()
                v.append(temp)
            flag += 1

        # Adjust flag for diagonals starting from columns
        flag = 0 if m % 2 == 0 else 1

        # Traverse diagonals starting from columns of last row
        for i in range(n - 1):
            j, k = m - 1, i + 1
            temp = []
            while j >= 0 and k < n:
                temp.append(mat[j][k])
                j -= 1
                k += 1
            if flag % 2 == 0:
                v.append(temp)
            else:
                temp.reverse()
                v.append(temp)
            flag += 1

        # Merge all diagonals into single result
        ans = []
        for diag in v:
            ans.extend(diag)

        return ans