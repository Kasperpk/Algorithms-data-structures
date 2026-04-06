def last_digit_of_fibonacci_number(n):
    '''
    The key insight is that we never need the full Fibonacci number.
    Because modular arithmetic distributes over addition,
    we can maintain the invariant that curr is always the last digit of Fₙ.
    This bounds integer growth and reduces the algorithm from exponential
    bit complexity to constant space and linear time.
    '''
    n %= 60  # Pisano period for mod 10

    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(1, n):
        prev, curr = curr, (prev + curr) % 10

    return curr

if __name__ == '__main__':
    n = int(input())
    fibonacci_number = last_digit_of_fibonacci_number(n)
    result = str(fibonacci_number)[-1]
    print(result)
