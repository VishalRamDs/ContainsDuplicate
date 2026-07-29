class Solution(object):
    def firstUniqChar(self, s):
       seen={}
       #Counting the occurance
       for char in s:   
           seen[char]=seen.get(char,0)+1
           
       #Spot the first recurring char
       for i,char in enumerate(s):
           if seen[char] == 1:
               return i

       return -1