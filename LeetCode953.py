'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.
'''

def isAlienSorted(words, order):
    order_values = {order[i]: i for i in range(len(order))}
    
    for i in range(0, len(words)-1):
        word1, word2 = words[i], words[i+1] # Checamos cada par adyacente, ya que por transitividad si i no está en orden, i + 2 no lo está
        
        j = 0
        while j < len(word1) and j < len(word2):
            
            if j == len(word2)-1 and word1[j] == word2[j] and len(word1) > len(word2): # Checamos el caso de que [apple, app]
                return False
            
            if order_values[word1[j]]  == order_values[word2[j]]: # Si los valores son iguales queremos checar los otros
                j += 1
            else:
                if order_values[word1[j]]  > order_values[word2[j]]:
                    return False 
                else:
                    break
            
    return True

words = ["hello","hello"]
order = "abcdefghijklmnopqrstuvwxyz"

print(isAlienSorted(words, order))
        
        
        