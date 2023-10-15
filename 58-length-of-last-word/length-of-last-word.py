import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split function
        '''
        new_list = s.strip().split(' ')
        return len(new_list[-1])
        '''

        # Previous simple
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

        # Regular expression
        '''
        pattern = r'([a-zA-Z]+)\s*$'
        match = re.search(pattern, s)
        return len(match.group(1))
        '''