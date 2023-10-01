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
        if not words:
            return result
        result = []
        word_len = len(words[0])
        words_len = len(words)
        string_len = len(s)
        correct_answer = collections.Counter(words)
        i = 0

        while i <= string_len - (word_len * words_len):
            a = s[i:i + word_len]
            if a in words:
                curr = {word : 0 for word in correct_answer}
                curr[a] += 1
                j = i + word_len
                counter = 1
                while j <= string_len - (word_len * (words_len - counter)):
                    a = s[j:j + word_len]
                    if a in curr and curr[a] < correct_answer[a]:
                        curr[a] += 1
                        counter += 1
                        j = j + word_len
                    else:
                        break
                if curr == correct_answer:
                    result.append(i)
            i += 1
        return result
