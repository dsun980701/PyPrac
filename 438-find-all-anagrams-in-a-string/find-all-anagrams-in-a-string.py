class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Initial answer using collections.Counter, a sub-dict object
        '''
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
        '''
        # optimized answer using hash
        len_p, len_s = len(p), len(s)
        if len_p > len_s:
            return []
        correct_hash_sum, curr_hash_sum  = 0, 0
        for i in range(len_p):
            correct_hash_sum += hash(p[i])
            curr_hash_sum += hash(s[i])
        result = []
        if correct_hash_sum == curr_hash_sum:
            result.append(0)
        i = len_p
        while i < len_s:
            curr_hash_sum -= hash(s[i - len_p])
            curr_hash_sum += hash(s[i])
            if correct_hash_sum == curr_hash_sum:
                result.append(i - (len_p - 1))
            i += 1
        return result