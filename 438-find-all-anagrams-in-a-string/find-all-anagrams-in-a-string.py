class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p) - 1
        len_s = len(s)
        correct = collections.Counter(p)
        check = collections.Counter(s[:len_p])
        result = []
        i = len_p
        while i < len_s:
            check[s[i]] += 1
            if check == correct:
                result.append(i - len_p)
            check[s[i - len_p]] -= 1
            i += 1
        return result
                
