'''
Given two strings s1 and s2, return true if s2 contains the permutation of s1.

In other words, one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

 

Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.


'''
# Este problema si uno lo piensa de una manera un poco fácil de hacer si generamos todas las subcadenas
# de s2 de tamaño len(s1) y checamos si estas subcadenas contienen la misma cantidad de letras que s2

# Pero eso es muy ineficiente ya son n / m subcadenas con n => m y luego andar checando es también muy tardado
# Por lo que acababamos con un complejidad de O(n^2 *m)



# Para hacer esto O(n + m) lo que hay que hacer es usar 
# la técnica de Sliding Window

# Lo que hacemos es mantener una ventana de tamaño m = len(s1) sobre la cadena s2
# De esta forma vamos chacando cada subcadena de tamaño m si es un permutación de s1

# Esto lo hacemos con un Diccionario contando la frecuencia de cada caracter en s1, es decir

# En el ejemplo s1 = "ab", s2 = "eidbaooo"

#       Nuestro Diccionario se ve asi {a: 1, b: 2, c:0, ...}

# El  truco es cada vex que veamos un nuevo caracter en nuestra ventana
# disminuyamos la frecuencia en el diccionario

# Los caracteres que no estén s1 nunca serán positivas, de manera que para
# aseguraramos de que sólo los caracteres en s1 se tomen en cuentan,
# ya que estos siempre serán positivos al momento de que los visitemos en
# nuesta ventana

def checkInclusion(self, s1: str, s2: str) -> bool:
    aux_s = "abcdefghijklmnñopqrstuvwxyz"
    hash_arr = {c:0 for c in aux_s}
        
    # Add the how many times the char in s1 appear
    for c in s1:
        hash_arr[c] += 1  
    
    start, n = 0, len(s1)
    aux_cont = n
    for end in range(len(s2)):
        if(end - start >= n): # When we have of window of lenght == len(s1)
            char = s2[start]
            
            hash_arr[char] += 1 # Increment cause we're not longer using this char in our window
                
            if hash_arr[char] > 0: # In case the char at start is in s1
                aux_cont += 1
            start += 1
                
        char = s2[end]
        hash_arr[char] -= 1 # Decrement because now this char is inside pur window
            
        if hash_arr[char] >= 0: # In case the char at start is in s1
            aux_cont -= 1
            
        if aux_cont == 0:
            return True
            
    return False