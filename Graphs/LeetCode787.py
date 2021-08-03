'''
There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that 
there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, 
return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
'''
from heapq import heapify, heappush, heappop
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        neighbors = defaultdict(list)
        for ticket in flights:
            neighbors[ticket[0]].append((ticket[1], ticket[2]))
        
        heap = [(0, src)]
        heapify(heap)
        while heap:
            print(heap)
            dist, v = heappop(heap)
            if v == dst:
                return dist
            if k+1 > 0:
                for n in neighbors[v]:
                    heappush(heap, (n[1]+dist, n[0]))
                k -= 1
        
        return -1
    
sol = Solution()
n = 3 
flights = [[0,1,100],[1,2,100],[0,2,500]] 
src = 0 
dst = 2 
k = 0
print(sol.findCheapestPrice(n, flights, src, dst, k))
            
            
        
                
            
            
            
        
            
            