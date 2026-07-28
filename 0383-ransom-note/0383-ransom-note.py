class Solution(object):
    def canConstruct(self, ransomNote, magazine):        
        Count={}
        for char in magazine:
            Count[char] = Count.get(char,0)+1

        for char in ransomNote:
            if char not in Count:
                return False
            Count[char]-=1

            if Count[char]<0:
                return False
        
        return True   

        
        