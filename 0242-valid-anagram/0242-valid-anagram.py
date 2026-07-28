class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        
        Count={}
        #Count occurance of each charecter
        for char in s:
            Count[char]=Count.get(char,0)+1

        #Decreasing the count if comman char occurs
        for char in t:
            if char not in Count:
                return False
            Count[char]-=1
            if Count[char]<0:
                return False
        return True
       
               