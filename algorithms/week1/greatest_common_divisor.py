def greatest_common_divisor(a,b):
    if b == 0:
        return a
    a_prime = a%b
    return greatest_common_divisor(b, a_prime)

if __name__ == '__main__':
    a, b = map(int, input().split())
    result = greatest_common_divisor(a,b)
    print(result)