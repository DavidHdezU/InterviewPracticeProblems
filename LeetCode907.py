'''
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:

Input: arr = [11,81,94,43,3]
Output: 444

 

Constraints:

    1 <= arr.length <= 3 * 104
    1 <= arr[i] <= 3 * 104


'''


# El truco aquí es usar una Pila Monotona
# Ser monotona significa que sigue un órden dado, puedes pensar esto como el principio del buen órden

def left_elem(arr):
    left, stack = [1]*len(arr), []
    for i in range(len(arr)):
        while stack and arr[i] <= stack[-1][0]:
            left[i] += stack.pop()[1]
        stack.append((arr[i], left[i]))
    return left
print(left_elem([8, 3, 7, 4, 5, 2, 10])) # Deberia ser [1, 1, 1, 1, 1] ya que a la izquierda de cada elemento no hay elementos
                             # más grandes a la izquierda de cada uno, sólo se contaria el mismo elemento
                             
def right_elem(arr):
    right, stack = [1]*len(arr), []
    for i in range(len(arr)-1, -1, -1):
        while stack and arr[i] < stack[-1][0]:
            right[i] += stack.pop()[1]
        stack.append((arr[i], right[i]))
    return right
print(right_elem([8, 3, 7, 4, 5, 2, 10])) # Deberia ser [5, 4, 3, 2, 1]

# Elementos más grandes a la izquierda de 1 -> [2, 3, 4, 5], entonces son 4 + 1, ya que también se cuenta el mismo
# Elementos más grandes a la izquierda de 2 -> [3, 4, 5], entonces son 3 + 1, ya que también se cuenta el mismo
# Elementos más grandes a la izquierda de 3 -> [4, 5], entonces son 2 + 1, ya que también se cuenta el mismo
# Elementos más grandes a la izquierda de 4 -> [5], entonces son 1 + 1, ya que también se cuenta el mismo
# Elementos más grandes a la izquierda de 5 -> [], entonces son 0 + 1, ya que también se cuenta el mismo



# Entonces al calcular los arreglos left y right, estos nos dicen cuantos subarreglos existen
# tales que estos tienen como minimo al elemento en la posición i

# Entonces al final como decias, esto es el número de apariciones

# res = sum(arr[i] * (left[i]*right[i]))


def sumSubarrayMins(arr):
    left = left_elem(arr)
    right = right_elem(arr)
    
    res = 0
    for i in range(len(arr)):
        res += (arr[i] * (left[i]*right[i]))
        
    return int(res % (10**9 + 7))

print(sumSubarrayMins([1, 2, 3, 4, 5]))


# En realidad este problema para hacerlo en O(n) teniamos que tener conocimiento
# de esta la Monotone Stack :v