class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        list = [] # A list of past numbers

        for num in nums:
            if num in list:
                return True
            
            list.append(num)
        
        return False
