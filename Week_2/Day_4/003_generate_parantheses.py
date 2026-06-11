from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def build(s, open_used, close_used):
            if len(s) == 2 * n:
                answer.append(s)
                return
            if open_used < n:
                build(s + "(", open_used + 1, close_used)
            if close_used < open_used:
                build(s + ")", open_used, close_used + 1)
        build("", 0, 0)
        return answer