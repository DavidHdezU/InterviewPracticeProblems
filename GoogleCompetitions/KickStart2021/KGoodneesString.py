def solve(s, k, n):
    count = 0
    for i in range(n):
        if s[i] == s[n-i+1]:
            count += 1
            
    return abs(count-k)


