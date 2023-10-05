class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mini = len(nums) / 3
        a = collections.Counter(nums)
        result = []
        for num, appearence in a.items():
            if appearence > mini:
                result.append(num)
        return result