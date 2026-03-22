#def distinct_numbers(numbers):
#    return len(set(numbers))

import sys
input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    numbers = map(int, input().split())
    print(len(set(numbers)))