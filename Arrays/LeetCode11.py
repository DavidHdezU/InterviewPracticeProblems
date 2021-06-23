'''
Given n non-negative integers a1, a2, ..., an ,
where each represents a point at coordinate (i, ai). n vertical lines 
are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
'''

class Solution:
    # Time Complexity -> O(n)
    # Space Complexity -> O(1)
    def maxArea(self, height): 
        # Iterar sobre todas las barras, ir actulizando
        # el maximo y cuando lo actualizemos calcular el area
        #, y actualizar la area_max en una variable
        
        max_area = 0
        l, r = 0, len(height)-1
        initial_max = max(height)  # To "optimeze" the solution we can't
                                            # stop the loop when we find a more greater area
        while initial_max*(r-l) > max_area:
            max_area = max(max_area, min(height[l], height[r]) * (r-l))
            
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        

        return max_area