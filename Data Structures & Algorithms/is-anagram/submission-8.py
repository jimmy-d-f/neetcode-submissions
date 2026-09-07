class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary_s = {}
        dictionary_t = {}

        for char_s in s:
            if char_s in dictionary_s:
                dictionary_s[char_s] += 1
            else:
                dictionary_s[char_s] = 1

        for char_t in t:
            if char_t in dictionary_t:
                dictionary_t[char_t] += 1

            else:
                dictionary_t[char_t] = 1

        return dictionary_s == dictionary_t