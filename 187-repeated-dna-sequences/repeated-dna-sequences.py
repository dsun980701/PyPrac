class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        s_len = len(s)
        if s_len < 10:
            return []
        counts = collections.Counter()
        i = 0
        deck = deque(s[:10], maxlen=10)
        counts[''.join(deck)] += 1 
        for char in s[10:]:
            deck.append(char)
            counts[''.join(deck)] += 1
        result = []
        for key, val in counts.items():
            if val >= 2:
                result.append(key)
        return result

