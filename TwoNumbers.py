class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # val : index
        for i, n in enumerate(nums):
            if n<=target:
                diff = target-n
                if diff in hashmap:
                    return [hashmap[diff],i]
                hashmap[n]=i
        return