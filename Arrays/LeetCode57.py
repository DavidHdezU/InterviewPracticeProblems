'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''


class Solution:
    # Buscamos donde insertar el nuevo intervalo, para no tener que ordenarlo de nuevo
    def insert_interval(self, intervals, new_interval):
        i = 0
        while i < len(intervals) and new_interval[0] >= intervals[i][0]:
            i += 1
        intervals.insert(i, new_interval) # O(n)
        
    def insert(self, intervals, newInterval): # O(n)
        if not intervals:
            return [newInterval]
        
        self.insert_interval(intervals, newInterval)
        res = [intervals[0]]
        
        # Después sólo es como el ejercicio de Merge Intervals
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
                if intervals[i][0] < res[-1][0]: # El único caso especial es cuando en i tenemos un inicio más pequeño
                    res[-1][0] = intervals[i][0]
            else:
                res.append(intervals[i])
        
        return res
        
        
        
sol = Solution()
intervals = [[1,3],[6,9]]
new_interval = [2,5]   
print(sol.insert(intervals, new_interval))
            
                

        
            
            