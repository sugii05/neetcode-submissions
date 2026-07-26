class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashting = set(nums)
        n = len(nums)
        streak = 0
        longest = 0

        

        for i in nums:
            if i-1 not in hashting: 
                streak = 1
                temp = i+1
                while temp in hashting:
                    temp += 1
                    streak += 1

                longest = streak if streak > longest else longest 
            
        
        return longest

                


                 







        