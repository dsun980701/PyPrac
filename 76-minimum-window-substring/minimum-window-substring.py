class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
    # First answer
        m = len(t)
        correct = collections.defaultdict(int)
        for char in t:
            correct[char] += 1
        keys_correct = correct.keys()
        start = 0
        s_len = len(s)
        result = collections.defaultdict(int)
        i, start = 0, 0
        mini = 999999
        sub = ''
        while i < s_len:
            if all([result[key] >= correct[key] for key in keys_correct]):
                if mini > i - start:
                    mini = i - start
                    sub = s[start:i]
                    if mini == m:
                        return sub
                result[s[start]] -= 1
                start += 1
            else:
                result[s[i]] += 1
                i += 1
        while True:
            if all([result[key] >= correct[key] for key in keys_correct]):
                if mini > i - start:
                    mini = i - start
                    sub = s[start:i]
                result[s[start]] -= 1
                start += 1
            else:
                break
        return sub
        '''
    # Second answer optimizing the requirement check 
        correct = collections.Counter(t)  
        required = len(correct)
        l, r = 0, 0  # left and right pointers
        formed = 0  
        result = collections.defaultdict(int)
        #ans =  (minimum window length, left, right)
        ans = 999999999, None, None  
        while r < len(s):
            char = s[r]
            result[char] += 1
            if char in correct and result[char] == correct[char]:
                formed += 1
            while l <= r and formed == required:
                char = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                result[char] -= 1
                if char in correct and result[char] < correct[char]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == 999999999 else s[ans[1]: ans[2] + 1]
