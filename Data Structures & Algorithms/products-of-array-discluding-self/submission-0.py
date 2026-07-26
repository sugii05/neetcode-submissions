class Solution:
    def create_prefix(self, nums: List[int]) -> List[int]:
        pref = [1]
        c = 1

        for i in nums:
            c *= i
            pref.append(c)
        
        return pref

    def create_suffix(self,nums: List[int]) -> List[int]:
        
        n = len(nums)
        suff = [1] * n
        k = 1

        for i in range(n-1, -1, -1):
            k = k*nums[i]
            suff[i] = k

        suff.append(1)
        
        return suff
    def productExceptSelf(self, nums: List[int]):
        left = self.create_prefix(nums)
        right = self.create_suffix(nums)
        anss = []
        for i in range(1,len(left)):
            ans = left[i-1]*right[i]
            anss.append(ans)
        return anss




        

            
        
        




        
        





