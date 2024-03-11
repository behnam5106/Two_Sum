class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        print(hashmap)
        for i in range(len(nums)):
            complement = target - nums[i]
            print (complement)
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 
            
nums=[-3,4,3,90]
target=0
solution=Solution()
result=solution.twoSum(nums,target)
print(result)