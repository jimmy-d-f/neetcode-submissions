class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        list = []
        
        for num in nums:
            if num in list:
                return True
            list.append(num)

        return False