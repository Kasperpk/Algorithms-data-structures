def permutations(n):
    '''
    Function that returns the possible permutations of n
    '''    
    if n > 1 and n <= 3:
        return "NO SOLUTION"
    
    permutations = []
    start = 2
    while start <= n:
        permutations.append(start)
        start+=2

    start = 1
    while start <= n:
        permutations.append(start)
        start+=2

    if len(permutations) == n:
        return permutations
    else:
        return "NO SOLUTION"
    

if __name__ == '__main__':
    n = int(input())
    result = permutations(n)
    if type(result) == list:
        print(' '.join(str(num) for num in result))
    else:
        print(result)