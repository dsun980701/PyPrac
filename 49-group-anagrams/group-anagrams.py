class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use hash function
        a = collections.defaultdict(list)
        for string in strs:
            key = 0
            for char in string:
                key += hash(char)
            a[key].append(string)
        return [a[key] for key in a]