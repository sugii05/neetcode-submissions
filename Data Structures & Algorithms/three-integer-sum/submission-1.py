class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        reslt = []
        nums.sort()
        length = len(nums)

        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                l, r = i+1, length-1
                target = -(nums[i])

                while l < r:
                    if nums[r]+nums[l] > target:
                        r -= 1
                    elif nums[r]+nums[l] < target:
                        l += 1
                    else:
                        reslt.append([nums[i], nums[l], nums[r]])
                        r-=1
                        while nums[r] == nums[r+1] and l < r:
                            r-=1
        
        return reslt



                        

                        
                        

                    





                













        