class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] = freq[num] + 1
        
        result = []
        
        for i in range(k):
            max_num = None
            max_count = 0
            
            for num in freq:
                if freq[num] > max_count:
                    max_count = freq[num]
                    max_num = num
            
            result.append(max_num)
            del freq[max_num]
        
        return result