def pisano_period(m):
    prev, curr = 0, 1
    for i in range(m * m):
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            return i + 1


def fib_mod(n, m):
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % m
    return curr


if __name__ == '__main__':
    n, m = map(int, input().split())

    period = pisano_period(m)
    n = n % period

    print(fib_mod(n, m))
