class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Previous Answer using counter
        '''
        s_len = len(s)
        if s_len < 10:
            return []
        counts = collections.Counter()
        result = []
        deck = deque(s[:10], maxlen=10)
        counts[''.join(deck)] += 1 
        for char in s[10:]:
            deck.append(char)
            tm = ''.join(deck)
            counts[tm] += 1
            if counts[tm] == 2:
                result.append(tm)
        return result
        '''
        # Answer using HashTable
        s_len = len(s)
        if s_len < 10:
            return []
        counts = collections.defaultdict(int)
        result = []

        for i in range(s_len - 9):
            dna = s[i:i+10]
            counts[dna] += 1
            if counts[dna] == 2:
                result.append(dna)

        return result

