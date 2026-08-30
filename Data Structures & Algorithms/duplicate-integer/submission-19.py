class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for int in nums:
            if int in seen:
                return True
            
            seen.add(int)

        return False

