def fib_last_digit(n):
    n %= 60  # Pisano period for mod 10
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(1, n):
        prev, curr = curr, (prev + curr) % 10
    return curr


if __name__ == '__main__':
    n, m = map(int, input().split())

    result = fib_last_digit(m + 2) - fib_last_digit(n + 1)
    print(result % 10)