class Solution:
    def minWindow(self, s: str, t: str) -> str:
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
