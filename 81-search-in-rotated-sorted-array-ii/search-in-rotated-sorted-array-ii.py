class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            num_mid, num_r, num_l  = nums[mid], nums[r], nums[l]
            if num_mid == target:
                return True
            # Since there are duplicates, and we aren't sure wheter the numbers
            # in between indx-mid and indx-r is all identical or it is part of the
            # reversed array, we need to simply move the bound of the r
            if num_mid == num_r:
                r -= 1
            #Left half of the currently scrutinized range is sorted
            elif num_mid > num_r:
                # Target located within the left sorted array
                if num_l <= target < num_mid:
                    r = mid - 1
                # Target located within the right array, where it is not fully sortted
                else:
                    l = mid + 1
            # Right half of the currently scrutinized range is sorted
            else:
                # Situated on the right
                if num_mid < target <= num_r:
                    l = mid + 1
                else:
                    r = mid - 1
        return False