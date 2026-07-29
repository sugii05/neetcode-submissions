class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered = [x for x in s if x.isalnum()]

        new = "".join(filtered)
        new = new.lower()

        for i in range((len(new)+1)//2):
            if new[i] != new[len(new)-i-1]:
                return False
        
        return True
        



        