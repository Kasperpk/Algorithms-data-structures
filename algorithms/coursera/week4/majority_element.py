def majority_element(numbers):
    for number in numbers:
        if numbers.count(number) > int(len(numbers)/2):
            return 1
        return 0


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    result = majority_element(numbers)
    print(result)