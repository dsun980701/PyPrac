class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [-1,-1]
        len_nums = len(nums)
        l, r = 0, len_nums - 1
        while r >= l:
            mid = (r+l) // 2
            num = nums[mid]
            if num > target:
                r = mid - 1
            elif num < target:
                l = mid + 1
            else:
                answer = [mid,mid]
                i = mid + 1
                j = mid - 1
                while i < len(nums) and nums[i] == num:
                    answer[1] += 1
                    i += 1
                while j >= 0 and nums[j] == num:
                    answer[0] -= 1
                    j -= 1
                break
        return answer
