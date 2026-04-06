#def fibonacci_greedy(n):
#    if n <= 1:
#        return n
#
#    return fibonacci_greedy(n-1) + fibonacci_greedy(n-2)

#def fibonacci(n):
#  if n == 1 or n == 2:
#    return 1
#
#  fib_nums = {0:0, 1:1, 2:1}
#  for i in range(2, n+1):
#      first_num = i-1
#      second_num = i-2
#      fib_nums[i] = fib_nums[first_num] + fib_nums[second_num]
#  return fib_nums[n]
#
#if __name__ == '__main__':
#    n = int(input())
#    result = fibonacci(n)
#    print(result)

def fibonacci(n):
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(1, n):
        prev, curr = curr, prev + curr

    return curr

if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))


