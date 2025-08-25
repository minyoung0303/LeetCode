class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        r,c=len(mat),len(mat[0])
        # inilitize the result
        result=[]
        row=col=0
        for _ in range(r*c):
            result.append(mat[row][col])
            if(row+col)%2==0:
                if col==c-1:
                    row+=1
                elif row==0:
                    col+=1
                else:
                    row-=1
                    col+=1
            else:
                if row==r-1:
                    col+=1
                elif col==0:
                    row+=1
                else:
                    row+=1
                    col-=1
        return result

        return ans