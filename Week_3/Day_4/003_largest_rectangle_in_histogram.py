class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i

                ans = max(ans, h * w)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]

            if stack:
                w = len(heights) - stack[-1] - 1
            else:
                w = len(heights)

            ans = max(ans, h * w)

        return ans