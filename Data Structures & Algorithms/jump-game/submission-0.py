class Solution:
    def canJump(self, nums: List[int]) -> bool:

        maxReach = 0

        for i in range(len(nums)):

            if i > maxReach:
                return False

            maxReach = max(maxReach, i + nums[i])

        
        return True

'''

maxReach = 3
max(1, 1+2)

[1,2,0,1,0]
     ^
 

1 -> 2

2 -> 0,1


'''