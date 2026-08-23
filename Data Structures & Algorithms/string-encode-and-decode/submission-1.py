class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + '#' + s)
        return ''.join(encoded)
    
    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        
        while i < len(s):
            # Read length until '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract length
            length = int(s[i:j])
            
            # Extract string using length
            string_start = j + 1
            string_end = string_start + length
            result.append(s[string_start:string_end])
            
            # Move to next string
            i = string_end
        
        return result