def binary_search_with_duplicates(numbers, target):
    left = 0
    right = len(numbers)-1

    while right >= left:
        middle = int((left+right)/2)
        if numbers[middle] == target:
            index = numbers.index(target)
            return index
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    m = int(input())
    targets = list(map(int, input().split()))
    output = []
    for target in targets:
        output.append(binary_search_with_duplicates(numbers, target))
    print(output)