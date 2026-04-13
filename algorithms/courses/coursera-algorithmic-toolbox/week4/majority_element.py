def majority_element(numbers):

    numbers_count = {number: 0 for number in numbers}

    for number in numbers:
        numbers_count[number] += 1

    for number in numbers:
        if numbers_count[number] > int(len(numbers)/2):
            return 1
    return 0

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    result = majority_element(numbers)
    print(result)