class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = -1
        n = len(s)
        count = 0
        while i >= -n:
            char = s[i]
            if char.isalpha():
                count += 1
            if count and char == ' ':
                break
            i -= 1
        return count