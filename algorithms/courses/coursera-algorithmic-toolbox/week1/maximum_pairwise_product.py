def maximum_pairwise_product(n, integers):
    max_1 = max_2 = 0
    for integer in integers:
        if integer > max_1:
            max_2 = max_1
            max_1 = integer
        elif integer > max_2:
            max_2 = integer

    return max_1 * max_2


if __name__ == '__main__':
    n = int(input())
    integers = list(map(int, input().split()))
    result = maximum_pairwise_product(n, integers)
    print(result)