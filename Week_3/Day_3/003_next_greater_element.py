class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for x in nums1:
            i = nums2.index(x)

            greater = -1

            for j in range(i + 1, len(nums2)):
                if nums2[j] > x:
                    greater = nums2[j]
                    break

            ans.append(greater)

        return ans
        