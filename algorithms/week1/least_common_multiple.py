def least_common_multiple(a,b):

    def greatest_common_divisor_euclid(a, b):
        if b == 0:
            return a
        a_prime = a % b
        return greatest_common_divisor_euclid(b, a_prime)


    gcd = greatest_common_divisor_euclid(a,b)
    return int((a*b)/gcd)

if __name__ == '__main__':
    a, b = map(int, input().split())
    result = least_common_multiple(a,b)
    print(result)