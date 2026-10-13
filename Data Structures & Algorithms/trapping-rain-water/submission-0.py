class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0
        L = 0
        R = len(height) - 1

        leftMax = height[L]
        rightMax = height[R]

        while L < R:
            leftMax = max(leftMax, height[L])
            rightMax = max(rightMax, height[R])

            if leftMax < rightMax: 
                res += leftMax - height[L]
                L += 1
            else:
                res += rightMax - height[R]
                R -= 1
        
        return res





    # L = 0 
    # R = len(height) - 1

    # res = 0

    # leftMax = height[L]
    # rightMax = height[R]


    # while L < R:

        # update Left MAx the current left max and the height array at the left pointer 
        # update right MAx the current right max and the height array at the right pointer 

        # If the left max is smaller than the right max 
            # Calculate the water from the left. 
            # 






    # water = (R - L - 1) * min(height[L], height[R])



