class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        flat = []
        for row in mat:
            for num in row:
                flat.append(num)
        ans = []
        idx = 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(flat[idx])
                idx += 1
            ans.append(row)
        return ans        