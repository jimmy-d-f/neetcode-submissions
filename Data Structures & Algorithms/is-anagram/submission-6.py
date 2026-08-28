class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary_s = {}
        dictionary_t = {}

        for letter_s in s:
            if letter_s in dictionary_s:
                dictionary_s[letter_s] += 1
            else:
                dictionary_s[letter_s] = 1

        for letter_t in t:
            if letter_t in dictionary_t:
                dictionary_t[letter_t] += 1
            else:
                dictionary_t[letter_t] = 1


        return dictionary_s == dictionary_t
