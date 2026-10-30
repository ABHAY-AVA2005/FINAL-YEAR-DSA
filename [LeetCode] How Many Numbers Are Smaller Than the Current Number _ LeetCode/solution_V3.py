class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # sort and clone 
        sorted_nums=sorted(nums)

        map={}
        for i,num in enumerate(sorted_nums):
            if num not in map:
                map[num]=i
        
        return [map[num] for num in nums]
