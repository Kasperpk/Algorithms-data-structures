def maximum_salary(integers):
    sorted_integers = sorted(integers,reverse=True)
    return ''.join([str(integer) for integer in sorted_integers])


if __name__ == '__main__':
    n = int(input())
    integers = list(map(int, input().split()))
    result = maximum_salary(integers)
    print(result)

