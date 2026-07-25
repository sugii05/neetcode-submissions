class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashfreq = dict()
        freq = []
        n = len(nums)
        for _ in range(n+1):
            freq.append([])
        
        for num in nums:
            if num not in hashfreq:
                hashfreq[num] = 1
            else:
                hashfreq[num] += 1

        for i, cnt in hashfreq.items():
            freq[cnt].append(i)
        
        r = []
        cc = 0
        i = len(freq) - 1

        while cc < k:
            if not freq[i]:
                i -= 1
            else:
                val = freq[i].pop()
                r.append(val)
                cc += 1
                if not freq[i]:
                    i -= 1
        return r