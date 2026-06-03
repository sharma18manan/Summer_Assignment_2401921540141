class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr=[]
        for i in range(len(nums)):
            sqr.append(nums[i]*nums[i])
        return sorted(sqr)