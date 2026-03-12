def insertion_sort(n, numbers):

    for i in range(1, n):
        key = numbers[i]
        j = i-1
        while j >= 0 and numbers[j] > key:
            numbers[j+1] = numbers[j]
            j= j - 1
        numbers[j+1] = key
    return numbers

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    result = insertion_sort(n=n, numbers=numbers)
    print(result)