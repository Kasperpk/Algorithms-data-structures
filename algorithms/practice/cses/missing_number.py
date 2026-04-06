def missing_number(numbers):
    sorted_numbers = sorted(numbers)
    for index in range(0, len(sorted_numbers)-1):
        if sorted_numbers[index] - sorted_numbers[index+1] < -1:
            return sorted_numbers[index] + 1  
        
if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    result = missing_number(numbers)
    print(result)
    
    