class Solution:
    def maxArea(self, height: List[int]) -> int:
        # height * width

        maxArea = 0
        l = 0
        r = len(height) - 1       
        
        while l < r:
            newheight = min(height[l],height[r])
            width = r - l 
            maxArea = max(maxArea, newheight*width)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxArea 