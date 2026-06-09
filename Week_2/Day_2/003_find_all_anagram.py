class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        need = {}
        window = {}
        for ch in p:
            need[ch] = need.get(ch, 0) + 1
        for ch in s[:len(p)]:
            window[ch] = window.get(ch, 0) + 1
        ans = []
        if window == need:
            ans.append(0)
        left = 0
        for right in range(len(p), len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
            if window == need:
                ans.append(left)
        return ans