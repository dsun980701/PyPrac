class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # Hash method, slow
        '''
        len_colors = len(colors)
        if len_colors < 3:
            return False 
        a_count, b_count = 0, 0
        a = hash("A") + hash("A") + hash("A")
        b = hash("B") + hash("B") + hash("B")
        curr = sum(hash(color) for color in colors[:3])
        if curr == a:
            a_count += 1
        elif curr == b:
            b_count += 1
        i = 2
        while i < len(colors)-1:
            curr -= hash(colors[i-2])
            curr += hash(colors[i+1])
            if curr == a:
                a_count += 1
            elif curr == b:
                b_count += 1
            i += 1
        return a_count > b_count
        '''
        #Counter method
        '''
        a_count, b_count = 0, 0
        a = collections.Counter('AAA')
        b = collections.Counter('BBB')
        curr = collections.Counter(colors[:3])
        if curr == a:
            a_count += 1
        elif curr == b:
            b_count += 1
        i = 2
        while i < len(colors)-1:
            curr[colors[i-2]] -= 1
            curr[colors[i+1]] += 1
            if curr == a:
                a_count += 1
            elif curr == b:
                b_count += 1
            i += 1
        return a_count > b_count
        '''
        '''
        # Direct Comparison
        a_count, b_count = 0, 0
        i = 1
        while i < len(colors)-1:
            if colors[i -1] == 'A' and colors[i] == 'A' and colors[i+1] == 'A':
                a_count += 1
            elif colors[i -1] == 'B' and colors[i] == 'B' and colors[i+1] == 'B':
                b_count += 1
            i += 1
        return a_count > b_count
        '''
        #Regular Expression
        a_count = sum(len(match.group()) - 2 for match in re.finditer(r'A{3,}', colors))
        b_count = sum(len(match.group()) - 2 for match in re.finditer(r'B{3,}', colors))
        return a_count > b_count
