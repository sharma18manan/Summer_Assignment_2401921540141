class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        add=0
        n=len(mat)
        for i in range(n):
            add=add+mat[i][i]
            add=add+mat[i][n-1-i]
        if(n%2==1):
            add=add-mat[n//2][n//2]
        return add       