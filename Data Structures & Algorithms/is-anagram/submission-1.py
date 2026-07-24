class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        
        hashset1 = dict()
      

        for l in s:
            if l in hashset1:
                hashset1[l] += 1

            else:
                hashset1[l] = 1
        
        for li in t:
            if li not in hashset1:
                return False
            else:
                hashset1[li] -= 1
                if hashset1[li] < 0:
                    return False
                
        return True

            
            
            

        
        



            





        
        