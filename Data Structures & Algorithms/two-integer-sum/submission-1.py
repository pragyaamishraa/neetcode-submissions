class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]'''
        
        seen = {}
        n = len(nums)
        for i in range(0,n):
            req = target - nums[i]
            if req in seen:
                return [seen[req],i]
            seen [nums[i]] = i