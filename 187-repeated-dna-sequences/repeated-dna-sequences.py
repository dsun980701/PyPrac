class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        s_len = len(s)
        if s_len < 10:
            return []
        counts = collections.Counter()
        result = []
        deck = deque(s[:10], maxlen=10)
        counts[''.join(deck)] += 1 
        for char in s[10:]:
            deck.append(char)
            counts[''.join(deck)] += 1
            if counts[''.join(deck)] == 2:
                result.append(''.join(deck))
        return result
        
 

