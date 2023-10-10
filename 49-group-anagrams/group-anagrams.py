class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        a = collections.defaultdict(list)
        for string in strs:
            # Use hash function as key
            '''
            key = 0
            for char in string:
                key += hash(char)
            '''
            # Use sorted string as key
            a["".join(sorted(string))].append(string)
        return [a[key] for key in a]