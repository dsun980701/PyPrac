class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        len_candidates = len(candidates)
        def combination(target, curr, start_indx):
            # Base Case
            if target == 0:
                result.append(curr)
                return
            for i in range(start_indx, len_candidates):
                if i > start_indx and candidates[i-1] == candidates[i]:
                    continue
                num = candidates[i]
                if num > target:
                    break
                combination(target - num, curr + [num], i+1)
        combination(target , [], 0)
        return result