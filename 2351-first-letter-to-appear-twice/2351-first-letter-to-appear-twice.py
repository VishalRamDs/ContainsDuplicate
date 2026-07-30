class Solution(object):
    def repeatedCharacter(self, s):
        seen=set()        
        #If char not in set --> add it in set, if char already in set --> return char
        for char in s:
            if char in seen:
                return char
            seen.add(char)
    
        