def fibonacci(n):
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(1, n):
        prev, curr = curr, prev + curr

    return curr

if __name__ == '__main__':
    n = int(input())
    sum = 0
    for i in range(0, n+1):
        sum = sum + fibonacci(i)
    result = str(sum)[-1]
    print(result)