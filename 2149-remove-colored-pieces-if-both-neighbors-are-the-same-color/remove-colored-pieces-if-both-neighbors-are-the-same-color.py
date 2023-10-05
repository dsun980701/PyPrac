class Solution:
    def winnerOfGame(self, colors: str) -> bool:
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
