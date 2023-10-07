class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        len_candidates = len(candidates)
        def find_sum(target, curr: List[int], start_idx: int):
            # Base Case
            if target == 0:
                result.append(curr[:])
                return
            elif target < 0:
                return
            # Problem Reduction
            for i in range(start_idx, len(candidates)):
                find_sum(target - candidates[i], curr + [candidates[i]], i) 
        find_sum(target, [], 0)
        return result