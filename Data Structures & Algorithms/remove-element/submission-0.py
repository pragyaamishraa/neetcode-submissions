class Solution:    
    def removeElement(self, nums: List[int], val: int) -> int:
        filtered_nums = []
        for i in nums:
            if i != val:
                filtered_nums.append(i)
        
        nums[:len(filtered_nums)] = filtered_nums
        return len(filtered_nums)