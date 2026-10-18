class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # Initialize left and right pointers.
        L = 0
        R = 0

        res = []

        q = deque()

        while R < len(nums):
            while q and nums[q[-1]] < nums[R]:
                q.pop()
            q.append(R)

            if L > q[0]:
                q.popleft()
            
            if (R + 1) >= k:
                res.append(nums[q[0]])
                L +=1
            R += 1
        
        return res

        # while the right pointer isn't at the end. 
            # Look at the first window and append the maximum. 
            # Move both pointers forward. 
        
''''
k = 3
[1,2,1,0,4,2,6]
 ^   ^


max = [2, 2, 4, 4, 6]
'''

# while loop
# When the right pointer gets to the end, we've evaluated all windows. 