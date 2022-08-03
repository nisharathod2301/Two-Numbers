class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # val : index
        for i, n in enumerate(nums):
            #if n<=target:  #Use this if input is only positive integers
                diff = target-n
                if diff in hashmap:
                    return [hashmap[diff],i]
                hashmap[n]=i
        return
