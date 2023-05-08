class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        l=len(mat)
        c=l-1
        for i in range(l):
            s=s+mat[i][i]
            s=s+mat[i][c]
            c=c-1
        mid=int(l/2)+1
        if l%2==0:
            return s
        else:
            return s-mat[mid-1][mid-1]
        
        
        