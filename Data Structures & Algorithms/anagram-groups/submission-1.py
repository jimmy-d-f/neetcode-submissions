class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # Create a blank dictionary

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in groups:
                groups[sorted_word] = []

            groups[sorted_word].append(word)
        
        return list(groups.values())

