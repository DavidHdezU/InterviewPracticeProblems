'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

'''
import math
from heapq import heapify, heappush, heappop

def distance(point):
    return math.sqrt((point[0])**2 + (point[1])** 2)
def kClosest(points, k): # O(n log k) en tiempo, en espacio O(k), será O(n) en el peor de los casos y O(n log n) en tiempo para el peor de los
    heap = []  # When we're trying to find the min k things we're are going to use a Max Heap
    heapify(heap)
    for point in points:
        print(heap)
        dis = -distance(point)
        if len(heap) < k:
            heappush(heap, (dis, point))
        else:
            if dis > heap[0][0]:
                heappop(heap)
                heappush(heap, (dis, point))
    res = []
    while heap:
        res.append(heap[0][1])
        heappop(heap)
    return res

points = [[1,3],[-2,2],[2,-2]] 
k = 2

print(kClosest(points, k))
