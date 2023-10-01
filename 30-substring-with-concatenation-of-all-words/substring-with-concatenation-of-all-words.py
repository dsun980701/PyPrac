class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Previous answer
        '''
        if not words:
            return result
        result = []
        word_len = len(words[0])
        words_len = len(words)
        string_len = len(s)
        i = 0
        while i <= string_len - (word_len * words_len):
            a = s[i:i + word_len]
            if a in words:
                tmp = words.copy()
                tmp.remove(a)
                j = i + word_len
                while j <= string_len - (word_len * len(tmp)):
                    a = s[j:j + word_len]
                    if a in tmp:
                        tmp.remove(a)
                        j = j + word_len
                    else:
                        break
                if not tmp:
                    result.append(i)
            i += 1
        return result
        '''
        '''
        #Counter, Dict optimized Answer
        if not words:
            return []
        result = []
        word_len = len(words[0])
        words_len = len(words)
        string_len = len(s)
        correct_answer = Counter(words)
        
        for offset in range(word_len):
            i = offset
            while i <= string_len - word_len * words_len:
                curr = Counter()
                for j in range(i, i + word_len * words_len, word_len):
                    word = s[j:j + word_len]
                    if word not in correct_answer:
                        i = j + word_len
                        break
                    curr[word] += 1
                    if curr[word] > correct_answer[word]:
                        i += word_len
                        break
                else: 
                    if curr == correct_answer:
                        result.append(i)
                    i += word_len
        return result
        '''
        #Sliding Window Algorithm Incorporation
        if not words:
            return []
        
        word_len = len(words[0])
        words_len = len(words)
        string_len = len(s)
        correct_answer = collections.Counter(words)
        result = []
        
        for i in range(word_len): 
            start = i
            curr = collections.Counter()
            for j in range(i, string_len - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in correct_answer:
                    curr[word] += 1
                    while curr[word] > correct_answer[word]:
                        curr[s[start:start+word_len]] -= 1
                        start += word_len
                    if j - start == word_len * (words_len - 1):
                        result.append(start)
                else:
                    curr.clear()
                    start = j + word_len
        return result
        

