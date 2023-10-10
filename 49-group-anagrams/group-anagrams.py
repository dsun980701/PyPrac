class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        a = collections.defaultdict(list)
        for string in strs:
            # Use hash function
            '''
            key = 0
            for char in string:
                key += hash(char)
            '''
            a["".join(sorted(string))].append(string)
        return [a[key] for key in a]