#def fibonacci_greedy(n):
#    if n <= 1:
#        return n
#
#    return fibonacci_greedy(n-1) + fibonacci_greedy(n-2)

def fibonacci_dp(n):
    '''
    :param n: integer input
    :return: the n'th fibonacci number
    '''
    if n <= 1:
        return n

    fib_dp = [0]*n

    fib_dp[0] = 0
    fib_dp[1] = 1

    for i in range(2, n):
        fib_dp[i] = fib_dp[i-1] + fib_dp[i-2]
    return fib_dp[n-1]

if __name__ == '__main__':
    n = int(input())
    result = fibonacci_dp(n)
    print(result)


