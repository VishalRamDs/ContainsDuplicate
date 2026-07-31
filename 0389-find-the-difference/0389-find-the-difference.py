class Solution(object):
    def findTheDifference(self, s, t):
       seen={}
       #adding element to dictionary
       for char in s:
            seen[char]=seen.get(char,0)+1
            
       #reviewing element
       for char in t:
           if char not in seen:
               return char 
           seen[char]-=1
           if seen[char]<0:
               return char          

        
        


        